from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import datetime, pytz, math
from .utils import *
from .tasks import updateAccount
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from decimal import Decimal


# Global Variables

currencies = (
    ('$', 'Dollar'),
    ('£', 'Pound'),
    ('€', 'Euro'),
    ('¥', 'Yen')
)

status = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('declined', 'Declined')
)

# Create your models here.
class CompanyInfo(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    site_domain = models.CharField(max_length=150, blank=False, null=False, help_text="site url/link i.e miningsite.com")
    logo = models.ImageField(upload_to="images/company", blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    currency = models.CharField(max_length=1, choices=currencies, default='$', blank=False, null=False)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2, default=0.1, blank=False, help_text='IN PERCENTAGE(%)')
    bitcoin_address = models.CharField(max_length=200, blank=True, null=True)
    usdt_address = models.CharField(max_length=200, blank=True, null=True, help_text='TRC20')
    account_name = models.CharField(max_length=100, blank=True, null=True, help_text="Funding Account Name")
    account_number = models.CharField(max_length=15, blank=True, null=True, help_text="Funding Account Number")
    account_bank = models.CharField(max_length=160, blank=True, null=True, help_text="Funding Account Bank")
    swift_code =  models.CharField(max_length=25, blank=True, null=True, help_text="Funding Account Swift Code (optional)")
    iban_code =  models.CharField(max_length=100, blank=True, null=True, help_text="Funding Account IBAN Number (optional)")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id and CompanyInfo.objects.exists():
            raise ValueError("This model cannot have two or more records")
        else:
            super().save(*args, **kwargs)


# Manager class for custom user
class UserManager(BaseUserManager):
    # Determines how to create our user model and validations
    def create_user(self, first_name, last_name, email, phone, nationality, timezone, password=None):
        # Use this check for as many field you want
        if not email:
            raise ValueError("email is required")
        if not first_name:
            raise ValueError("provide a first name")
        if not last_name:
            raise ValueError("provide a last name")


        user = self.model(
            # normalize_email ensures our email is properly formatted
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            nationality = nationality,
            timezone = timezone
        )
        # Generating accout number for user
        user.account_number = generateAcountNumber()
        # Setting password for user
        user.set_password(password)
        # Saving user to database
        user.save(using=self._db)
        # Creating welcome message For user
        notification = Notification.objects.create(user=user, message=f'Hello {user.first_name}, Thanks for joining {CompanyInfo.name}. Complete your verification to gain full access')
        notification.save()
        # Return user after saving
        return user

    # Determines how to create superuser
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone=None,
            nationality=None,
            timezone=None,
            password = password
        )
        # Generating accout number for user
        user.account_number = generateAcountNumber()
        # Granting permissions to the super user
        user.is_staff = True
        user.is_superuser = True
        # Saving user to database
        user.save(using=self._db)
        # Return user after saving
        return user
    

    '''
    Make sure to set this manager as the manager in your custom model
    objects = MyUserManager()
    '''


# Custom user model class
class User(AbstractBaseUser, PermissionsMixin):
    themes = (
        ("dark", "Dark"),
        ("light", "Light")
    )
    account_types = (
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('current', 'Current'),
    )
    first_name = models.CharField(verbose_name="first name", max_length=30, null=False, blank=False)
    last_name = models.CharField(verbose_name="last name", max_length=30, null=False, blank=False)
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True, null=False, blank=False)
    phone = models.CharField(verbose_name="phone number", max_length=15, blank=True, null=True)
    nationality = models.CharField(verbose_name="country", max_length=25, blank=True, null=True)
    # You need to save users timezone to convert transaction timeframes in UTC to that of user using django filters
    timezone = models.CharField(max_length=60, null=True, blank=True)
    account_type = models.CharField(max_length=15, choices=account_types, default="savings")
    account_number = models.CharField(max_length=10, unique=True, default=0, blank=False, null=False)
    pin = models.CharField(max_length=4, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False, blank=False)
    overdraft = models.DecimalField(max_digits=15, decimal_places=2, default=0, null=False, blank=False)
    # verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    theme = models.CharField(max_length=10, choices=themes, default="light")

    @property
    def sidebar_theme(self):
        theme = ""
        if self.theme == "dark":
            theme = "sidebar-dark"
        else:
            theme = "sidebar-light"
        return theme

    @property
    def navbar_theme(self):
        theme = ""
        if self.theme == "dark":
            theme = "navbar-dark"
        else:
            theme = "navbar-light"
        return theme

    @property
    def text_theme(self):
        theme = ""
        if self.theme == "dark":
            theme = "text-light"
        else:
            theme = "text-dark"
        return theme

    @property
    def theme_classes(self):
        theme = ""
        if self.theme == "dark":
            theme = "bg-dark text-light"
        else:
            theme = "bg-light text-dark"
        return theme

    @property
    def currency(self):
        return CompanyInfo.objects.last().currency

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        if self.user.full_name:
            name = self.user.full_name
        elif self.user.email:
            name = self.user.email
        else:
            name = '-'
        return name

    @property
    def user_balance(self):
        # This just returns the balance and currency denomination
        return f'{self.currency}{self.balance}'

    @property
    def user_overdraft(self):
        # This just returns the overdraft and currency denomination
        return f'{self.currency}{self.overdraft}'

    @property
    # Function to return TOTAL ACCOUNT BALANCE
    def total_balance(self):
        return round(self.balance + self.overdraft, 2)

    @property
    # Function to check if user has an active card
    def has_active_card(self):
        has_active_card = False
        if VirtualCard.objects.filter(user=self, status="active").exists():
            has_active_card = True
        return has_active_card

    @property
    # Function is set to true is user's kyc is approved automatically
    def is_verified(self):
        verified = False
        if self.kyc.status == "approved":
            verified = True
        return verified

    # Setting to determing what field to use as login parameter
    USERNAME_FIELD = "email"

    # Setting to set required fields
    REQUIRED_FIELDS = ["first_name", "last_name"]

    # Setting a manager for this custom user model
    objects = UserManager()

    # Setting to determine what field to show on our database
    def __str__(self):
        return self.full_name

    # Determines if signup user has permissions
    def has_perm(self, perm, obj=None):
        return True

    # Determines if the signed up user will have acccess to other models
    # In our app or project
    def has_module_perms(self, app_label):
        return True

    # Function to get url per user for sitemapping
    def get_absolute_url(self):
        return f'/user/{self.id}'

    '''
    Make sure to set this custom model as our user model in settings.py
    AUTH_USER_MODEL = "App.CustomUserModel"
    Make sure to delete previous migration files incase of errors
    Then make migrations
    '''


class KYC(models.Model):
    kyc_status = (
        ('null', 'Null'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined')
    )
    id_types = (
        (None, None),
        ('national id', 'National ID'),
        ('drivers license', 'Driver License'),
        ("int'l passport", "Int'l Passport")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    passport = models.ImageField(upload_to="images/kyc", blank=True, null=True)
    id_type = models.CharField(max_length=30, choices=id_types, default=None, null=True, blank=True)
    id_number = models.CharField(max_length=60, null=True, blank=True)
    id_upload = models.ImageField(upload_to="images/kyc", blank=True, null=True)
    status = models.CharField(max_length=8, choices=kyc_status, default='null')
    approved_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'approved':
            self.approved_date = datetime.datetime.now(tz=pytz.UTC)
        elif self.status == 'declined':
            self.passport = None
            self.id_type = None
            self.id_number = None
            self.id_upload = None
            self.approved_date = None
        super().save(*args, **kwargs)


class VirtualCard(models.Model):
    card_types = (
        (None, None),
        ('mastercard', 'Mastercard'),
        ('visa', 'Visa'),
        ('verve', 'Verve')
    )
    card_status = (
        ('null', 'Null'),
        ('pending', 'Pending'),
        ('declined', 'Declined'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    card_type = models.CharField(max_length=10, choices=card_types, default=None, null=True, blank=True)
    card_name = models.CharField(max_length=100, null=True, blank=True)
    card_number = models.CharField(max_length=19, null=True, blank=True)
    card_pin = models.CharField(max_length=4, null=True, blank=True)
    # This is the date after admin approves after confirming user's card payment 
    approved_date = models.DateField(null=True, blank=True)
    # This is calculated expiry date from approved date
    expiry_date = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=3, null=True, blank=True)
    status = models.CharField(max_length=10, choices=card_status, default='null', null=False, blank=False)

    '''
    The idea is to check for card expiry date each time a user tries to use the card
    if expired:
        delete the card
    else:
        perform transaction 
    '''

    def save(self, *args, **kwargs):
        if VirtualCard.objects.filter(user=self.user, status='active').exists():
            raise ValueError("This user already has an active card")
        else:
            if self.status == 'active':
                # Assigning Mastercard to user card
                self.card_type = 'mastercard'
                # Adding user full name as card name
                self.card_name = self.user.full_name
                # Generating card number 
                self.card_number = generateVirtualCardNumber()
                # Setting card pin to user default pin
                self.card_pin = self.user.pin
                # Generating cvv
                self.cvv = generateCVV()
                # Setting approved date to current date and time
                self.approved_date = datetime.datetime.now(tz=pytz.UTC)
                # Setting expiry date to date after 2 years
                self.expiry_date = self.approved_date + datetime.timedelta(days=365 *2)
                super().save(*args, **kwargs)
            elif self.status == 'expired':
                self.delete()


    @property
    def card_digits(self):
        # This is the card number without spaces
        return self.card_number.replace(" ","")

    
    @property
    def card_validity(self):
        if self.expiry_date:
            valid_till = self.expiry_date.strftime("%m/%y")
        else:
            valid_till = None
        return valid_till



class Payment(models.Model):
    payment_status = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined')
    )
    methods = (
        ('bank transfer', 'Bank Transfer'),
        ('bitcoin', 'Bitcoin'),
        ('usdt', 'USDT(TRC20)'),
    )
    purposes = (
        ('funding', 'Account Funding'),
        ('card', 'Virtual Card'),
        ('loan', 'Loan Payment'),
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING , null=False, blank=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    purpose = models.CharField(max_length=12, choices=purposes, default='funding', null=False, blank=False)
    method = models.CharField(max_length=20, choices=methods, default='usdt', null=False, blank=False)
    proof = models.ImageField(upload_to="images/payment", blank=True, null=True)
    status = models.CharField(max_length=12, choices=payment_status, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *arg, **kwargs):
        # If payment is approved then activate the card automatically on save
        if self.purpose == 'funding' and self.status == 'approved':
            self.user.balance += self.amount
            self.user.save()
        elif self.purpose == 'card' and self.status == 'approved':
            virtual_card = VirtualCard.objects.create(
                user=self.user,
                status='active'
            )
            virtual_card.save()
        super().save(*arg, **kwargs)



class Transaction(models.Model):
    transaction_status = (
        ('pending', 'Pending'),
        ('successful', 'Successful'),
        ('failed', 'Failed')
    )
    transaction_types = (
        ('debit', "Debit"),
        ('credit', "Credit")
    )
    descriptions = (
        ('transfer', 'Transfer'),
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('purchase', 'Purchase'),
        ('loan', 'Loan'),
    )
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING , related_name="sender", help_text="Initiator", null=True, blank=True)
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiver", help_text="Recipient", null=True, blank=True)
    description = models.CharField(max_length=10, choices=descriptions, default='transfer', null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    remark = models.TextField(max_length=60, help_text="Comment", null=True, blank=True)
    session_id = models.CharField(max_length=24, unique=True, null=True, blank=True)
    transaction_number = models.CharField(max_length=18, unique=True, null=True, blank=True)
    status = models.CharField(max_length=12, choices=transaction_status, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Date And Time Initiated")

    '''
    Transaction Type = "debit" if user == self.from_user
    Transaction Type = "credit" if user == self.to_user
    '''

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_amount}"

    @property
    def currency(self):
        if self.from_user:
            currency = self.from_user.currency
        else:
            currency = self.to_user.currency
        return currency

    @property
    def transaction_amount(self):
        return f'{self.currency}{self.amount}'

    def save(self, *arg, **kwargs):
        if self.status == 'successful':
            self.session_id = generateSessionID()
            self.transaction_number = generateTransactionNumber()
        super().save(*arg, **kwargs)


class Loan(models.Model):
    loan_status = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('closed', 'Closed'),
        ('declined', 'Declined'),
    )
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=False)
    user_monthly_income = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=1, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=False, blank=False)
    duration_in_months = models.IntegerField(null=False, blank=False)
    remark = models.TextField(max_length=2500, null=False, blank=True)
    interest = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    monthly_returns = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    total_returns = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=8, choices=loan_status, default="pending")
    date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(null=True, blank=True, help_text="This is the approved date of loan")
    end_date =  models.DateTimeField(null=True, blank=True, help_text="This field is calculated and depends on approved date and duration of loan")

    @property
    def loan_interest_rate(self):
        if self.duration_in_months <= 6:
            rate = 10
        elif self.duration_in_months > 6 and self.duration_in_months <= 12:
            rate = 15
        elif self.duration_in_months > 12 and self.duration_in_months <= 18:
            rate = 20
        elif self.duration_in_months > 18 and self.duration_in_months <= 24:
            rate = 35
        else:
            rate = 50
        return rate


    def save(self, *args, **kwargs):
        self.currency = self.user.currency

        if self.status == 'approved':
            self.interest = (Decimal(self.loan_interest_rate) / 100) * self.amount
            self.total_returns = Decimal(self.amount + self.interest)
            self.monthly_returns = Decimal(self.total_returns / self.duration_in_months)
            # Setting approved date to current date and time
            self.approved_date = datetime.datetime.now(tz=pytz.UTC)
            # Setting end date to date and time after loan period from approved date
            self.end_date = self.approved_date + datetime.timedelta(days=self.duration_in_months * 30)
            # Finally activating the loan
            self.status = 'active'
            # creating notification message
            message = f'Congrats {self.user.first_name}, your loan request has been approved. Ensure to pay on time to enhance your credit score for future loans'
            # Crediting user of loan amount
            updateAccount(self.user, "balance", "credit", self.amount, message)
            # Creating a transaction record
            transaction = Transaction.objects.create(
                to_user=self.user,
                description='loan',
                amount=self.amount,
                remark=f'Loan request successfully approved',
                status='successful'
            )
            transaction.save()
        elif self.status == "declined":
            # Updating loan status
            self.status = 'declined'
            # Notifying user
            notification = Notification.objects.create(
                user=self.user,
                message=f'Sorry {self.user.first_name}, your loan request was declined. Ensure you are verified and eligible for loan offers'
            )
            notification.save()
        super().save(*args, **kwargs)


class Notification(models.Model):
    date  = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    message = models.TextField(max_length=5000, null=False, blank=False)

    def __str__(self):
        return f"{str(self.date)} {self.user.full_name}"