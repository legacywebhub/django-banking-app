from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.urls import reverse_lazy, reverse
from .models import *
from .utils import *
from .tasks import *
from decimal import Decimal
import json, datetime, pytz
from django.contrib.sites.shortcuts import get_current_site
# Mailing imports
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# Auth imports
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm




############### GLOBAL VARIABLES ################

forbidden_message = "<h2>Oops.. server could not be located</h2>"
endpoint_url = 'https://newsapi.org/v2/everything?q=finance&apiKey=9ab989f35bb6450c8e2a717543c0c129'


############### GLOBAL FUNCTIONS ################

def getRecentTransactions(user):
    first_party = Transaction.objects.filter(from_user=user).order_by('-timestamp')[:10]
    third_party = Transaction.objects.filter(to_user=user).order_by('-timestamp')[:10]
    transactions = list(first_party) + list(third_party)
    return transactions[:15]


############### Create your views here. ################
@login_required
def account(request):
    # Checking if IP is authenticated
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_transactions = getRecentTransactions(request.user)
    recent_payments = Payment.objects.filter(user=request.user).order_by('-timestamp')[:15]
    notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company':company,
        'recent_transactions': recent_transactions,
        'crypto_transactions': recent_payments,
        'notifications': notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/dashboard.html', context)
    return response


@login_required
def fundAccount(request):
    # Checking if IP is authenticated
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company':company,
        'notifications': notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/fund_account.html', context)
    return response


@login_required
def payment(request, id):
    # Checking if IP is authenticated
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    payment = get_object_or_404(Payment, id=id)
    notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company':company,
        'notifications': notifications,
        'payment': payment
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/make_payment.html', context)
    return response


@login_required
def transactions(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    p = Paginator(Transaction.objects.filter(from_user=request.user).order_by('-timestamp'), 20)
    page = request.GET.get('page')
    transactions = p.get_page(page)
    page_list = range(1, transactions.paginator.num_pages + 1)

    context = {
        'company': company,
        'transactions': transactions,
        'notifications': recent_notifications
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/transactions.html', context)
    return response


@login_required
def viewTransaction(request, id):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    transaction = get_object_or_404(Transaction, id=id)
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'transaction': transaction,
        'notifications': recent_notifications
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/transaction.html', context)
    return response


@login_required
def viewLoan(request, id):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    loan = get_object_or_404(Loan, id=id)
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'loan': loan,
        'notifications': recent_notifications
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/transaction.html', context)
    return response


@login_required
def loanHistory(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    p = Paginator(Loan.objects.filter(user=request.user).order_by('-date'), 20)
    page = request.GET.get('page')
    loans = p.get_page(page)
    page_list = range(1, loans.paginator.num_pages + 1)

    context = {
        'company': company,
        'loans': loans,
        'page_list': page_list,
        'notifications': recent_notifications
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/loan_history.html', context)
    return response


@login_required
def creditHistory(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    p = Paginator(Transaction.objects.filter(to_user=request.user).order_by('-timestamp'), 20)
    page = request.GET.get('page')
    transactions = p.get_page(page)
    page_list = range(1, transactions.paginator.num_pages + 1)

    context = {
        'company': company,
        'transactions': transactions,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/credit_history.html', context)
    return response


@login_required
def debitHistory(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    p = Paginator(Transaction.objects.filter(from_user=request.user).order_by('-timestamp'), 20)
    page = request.GET.get('page')
    transactions = p.get_page(page)
    page_list = range(1, transactions.paginator.num_pages + 1)

    context = {
        'company': company,
        'transactions': transactions,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/debit_history.html', context)
    return response


@login_required
def transferHistory(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    p = Paginator(Transaction.objects.filter(from_user=request.user, description='transfer').order_by('-timestamp'), 20)
    page = request.GET.get('page')
    transactions = p.get_page(page)
    page_list = range(1, transactions.paginator.num_pages + 1)

    context = {
        'company': company,
        'transactions': transactions,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/transfer_history.html', context)
    return response


@login_required
def internalTransfer(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/internal_transfer.html', context)
    return response


@login_required
def domesticTransfer(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/domestic_transfer.html', context)
    return response


@login_required
def internationalTransfer(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/international_transfer.html', context)
    return response


@login_required
def usdtTransfer(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/usdt_transfer.html', context)
    return response


@login_required
def loanRequest(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    loans = Loan.objects.filter(user=request.user)
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'loans': loans,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/loan_request.html', context)
    return response


@login_required
def changeTransactionPin(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/change_pin.html', context)
    return response


@login_required
def puchaseVirtualCard(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]
    virtual_card = VirtualCard.objects.get(user=request.user)

    context = {
        'company': company,
        'notifications': recent_notifications,
        'card': virtual_card
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/card.html', context)
    return response


@login_required
def notifications(request):
    forbidden = authorizeUser(request.user)
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/notifications.html', context)
    return response


@login_required
def profile(request):
    forbidden = authorizeUser(request.user)
    user = request.user
    company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'user': user,
        'company': company,
        'notifications': recent_notifications,
    }
    if forbidden:
        response = HttpResponseForbidden(forbidden_message) 
    else:
        response = render(request, 'dashboard/profile.html', context)
    return response


def logout(request):
    pass


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('mining:password_change_success')



@login_required
def passwordChangeSuccess(request):
    # delete notifications of user > 3days
    deleteOldNotifications(request.user)
    #company = CompanyInfo.objects.last()
    recent_notifications = Notification.objects.filter(user=request.user).order_by('-date')[:3]

    context = {
        'company':company,
        'recent_notifications': recent_notifications
    }
    return render(request, 'dashboard/success.html', context)



#################### Pseudo views ####################

# View to process user theme
def processTheme(request):
    data = json.loads(request.body)
    user = request.user
    user.theme = data
    user.save()
    return JsonResponse("success", safe=False)


def sendOTP(request, otp):
    company = CompanyInfo.objects.last()
    user = request.user 

    try:
        html_content = render_to_string('email/email_otp.html', {'company':company, 'otp':otp})
        email = EmailMessage(
            f'One Time Password', 
            html_content, 
            company.email, 
            [user.email,]
        )
        email.content_subtype = 'html'
        email.fail_silently = False
        email.send()
        response = {'status':'success'}
    except Exception as e:
        response = {'status':'failed', 'message': f'Error: {e}'}
    return JsonResponse(response, safe=False)


def changePin(request):
    data = json.loads(request.body)
    new_pin = data['new-pin']

    try:
        user = request.user
        user.pin = new_pin
        user.save()
        response = {'status':'success'}
    except Exception as e:
        response = {'status':'failed', 'message': f'Error: {e}'}
    return JsonResponse(response, safe=False)


# View to add interest to all users account
def topupInterest(request):
    interest_rate = CompanyInfo.objects.last().interest_rate

    for user in User.objects.all():
        interest = round(Decimal(interest_rate/100) * user.balance)
        user.balance += interest
        user.save()
        notification = models.Notification.objects.create(
            user=user, 
            message=f"Congrats, an interest of ${interest} was added to your account"
        )
        notification.save()
    messages.success(request, f'An interest of {interest_rate}% was successfully added to all account balance')
    return redirect('admin:onlinebankingapp_companyinfo_changelist')


def blockUser(request, id):
    user = User.objects.get(id=id)

    if user.is_blocked:
        messages.info(request, 'User is already blocked')
    else:
        user.is_blocked = True
        user.save()
        messages.success(request, 'User was blocked successfully')
    return redirect('admin:onlinebankingapp_user_changelist')


def unblockUser(request, id):
    user = User.objects.get(id=id)

    if not user.is_blocked:
        messages.info(request, "User is already unblocked")
    else:
        user.is_blocked = False
        user.save()
        messages.success(request, 'User was unblocked successfully')
    return redirect('admin:onlinebankingapp_user_changelist')


def processKYC(request):
    if request.method == "POST":
        passport = request.FILES.get("passport")
        id_number = request.POST.get("id-number")
        id_type = request.POST.get("id-type")
        id_image = request.FILES.get("id-image")

        # Only people with null or declined KYC can apply
        # Hence pending or approved KYC users can't re-apply

        try:
            kyc = KYC.objects.get(user=request.user)

            if kyc.status == "pending":
                response = "You have already have a pending KYC application"
            elif kyc.status == "approved":
                response = "You are already verified"
            else:
                kyc.passport = passport
                kyc.id_type = id_type
                kyc.id_number = id_number
                kyc.id_upload = id_image
                kyc.status = "pending"
                kyc.save()
                response = "success"
        except Exception as e:
            response = "Unknown error occured while submitting application"
    return JsonResponse(response, safe=False)


def approveKYC(request, id):
    kyc = KYC.objects.get(id=id)

    if kyc.status == "approved":
        messages.info(request, 'KYC is already approved')
    else:
        kyc.status = "approved"
        kyc.save()
        messages.success(request, 'KYC was approved successfully')
    return redirect('admin:onlinebankingapp_kyc_changelist')


def declineKYC(request, id):
    kyc = KYC.objects.get(id=id)

    if kyc.status == "declined":
        messages.info(request, 'KYC is already declined')
    else:
        kyc.status = "declined"
        kyc.save()
        messages.success(request, 'KYC was declined successfully')
    return redirect('admin:onlinebankingapp_kyc_changelist')


def approveLoan(request, id):
    loan = Loan.objects.get(id=id)

    if loan.status == "approved" or loan.status == "active":
        messages.info(request, 'loan is already approved or active')
    else:
        loan.status = "approved"
        loan.save()
        messages.success(request, 'loan was approved successfully')
    return redirect('admin:onlinebankingapp_loan_changelist')


def declineLoan(request, id):
    loan = Loan.objects.get(id=id)

    if loan.status == "declined":
        messages.info(request, 'loan is already declined')
    else:
        loan.status = "declined"
        loan.save()
        messages.success(request, 'loan was declined successfully')
    return redirect('admin:onlinebankingapp_loan_changelist')


def approvePayment(request, id):
    payment = Payment.objects.get(id=id)

    if payment.status == "approved":
        messages.info(request, 'Card Payment is already approved')
    else:
        payment.status = "approved"
        payment.save()
        messages.success(request, 'Card Payment is approved successfully')
    return redirect('admin:onlinebankingapp_payment_changelist')



def declinePayment(request, id):
    payment = Payment.objects.get(id=id)
    payment.status = "declined"
    payment.save()
    messages.success(request, 'Card Payment is declined successfully')
    return redirect('admin:onlinebankingapp_payment_changelist')



def processPayment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        amount = Decimal(data['amount'])
        method = data['method']
        purpose = data['purpose']

        try:
            payment = Payment.objects.create(
                user = request.user,
                amount = amount,
                method = method,
                purpose = purpose
            )
            payment.save()
            response = {
                'status': "success",
                'message': f"Success",
                'payment-url': f'/account/payment/{payment.id}/' 
            }
        except Exception as e:
            response = {
                'status': "failed",
                'message': f"Error: {e}"
            }
        return JsonResponse(response, safe=False)



def processRegisteration(request):
    if request.method == "POST":
        company = CompanyInfo.objects.last()
        data = json.loads(request.body)
        first_name = data['firstname']
        last_name = data['lastname']
        username = data['username']
        email = data['email']
        phone = data['phone']
        nationality = data['nationality']
        city = data['city']
        timezone = data['timezone']
        password1 = data['password1']
        password2 = data['password2']

        if password2 == password1:
            try:
                email.index('@') and email.index('.')
            except ValueError:
                response = {
                    'status': 'error',
                    'message': 'Your email is not valid'
                }
                return JsonResponse(response, safe=False)
            else:
                if User.objects.filter(email=email).exists():
                    response = {
                        'status': 'error',
                        'message': 'Sorry this email has already been taken!'
                    }
                    return JsonResponse(response, safe=False)
                else:
                    if not User.objects.filter(username=username).exists():
                        # Saving user and user instances
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            phone=phone,
                            nationality=nationality,
                            city=city,
                            timezone=timezone,
                            password=password2,
                        )
                        user.save()
                        # Send verify/success email
                        try:
                            # current_site_domain = get_current_site(request).domain
                            # link = f'https://{current_site_domain}/user/verify/{user.id}'
                            subject = f'Welcome, {user.first_name.capitalize()}'
                            message = f'Your account was successfully created and you are now eligible to explore our ecosystem. Kindly sign in to get started!'
                            html_content = render_to_string('email_template.html', {'company':company, 'subject':subject, 'message':message})
                            email = EmailMessage(
                                f'Registeration Successful', 
                                html_content, 
                                company.email, 
                                [user.email,]
                            )
                            email.content_subtype = 'html'
                            email.fail_silently = False
                            email.send()
                        except Exception as e:
                            print(e)
                        response = {'status':'success', 'message': f'{user.first_name}, your account has successfully been created... you can now sign in!'}
                        return JsonResponse(response, safe=False)
                    else:
                        response = {'status':'error', 'message': 'This username has already been taken'}
                        return JsonResponse(response, safe=False)
        else:
            response = {'status':'error', 'message': 'Passwords does not match'}
            return JsonResponse(response, safe=False)


def processInternalTransfer(request):
    data = json.loads(request.body)
    account = data['account']
    account_number = data['account_number']
    amount = data['amount']
    remark = data['remark']

    if remark == '' or remark == ' ':
        remark = None

    if data['pin'] == request.user.pin:
        feedback = performInternalTransfer(request.user, account, account_number, amount, remark)
    else:
        feedback = 'Invalid Pin'
    response = {
        'response': feedback,
        'balance': request.user.balance,
        'overdraft': request.user.overdraft
    }
    return JsonResponse(response, safe=False)


def processLoanRequest(request):
    data = json.loads(request.body)
    amount = Decimal(data['amount'])
    duration = int(data['duration'])
    remark = data['remark']

    if remark == '' or remark == ' ':
        remark = None

    if Loan.objects.filter(user=request.user, status='pending').exists() or Loan.objects.filter(user=request.user, status='active').exists():
        response = {
            'status': 'error',
            'message': 'You already have a pending loan request',
        }
    else:
        try:
            loan = Loan.objects.create(
                user = request.user,
                amount = amount,
                duration_in_months = duration,
                remark = remark
            )
            loan.save()
            url = reverse('banking:loan_detail', args=[loan.id])
            response = {
                'status': 'success',
                'loan-id': loan.id,
                'loan-amount': loan.amount,
                'loan-duration': loan.duration_in_months,
                'loan-status': loan.get_status_display(),
                'loan-url': reverse('banking:loan_detail', args=[loan.id])
            }
        except Exception as e:
            response = {
                'status': 'failed',
                'message': f'Error: {e}',
            }
    return JsonResponse(response, safe=False)


# View to process message request
def processMessage(request):
    company = CompanyInfo.objects.last()
    data = json.loads(request.body)
    location = data['location']
    message = data['message']

    if request.user.is_authenticated:
        name = request.user.full_name
        email = request.user.email
        subject = 'Support'
    else:
        name = data['name']
        email = data['email']
        subject = data['subject']

    try:
        email.index('@') and email.index('.')
    except ValueError:
        response = {
            'status': 'error',
            'message': 'Your email is not valid'
        }
    else:
        try:
            html_content = render_to_string('email_template.html', {'subject':subject, 'message':message, 'company':company})
            email = EmailMessage(subject, html_content, email, [company.email, settings.EMAIL_HOST_USER])
            email.content_subtype = 'html'
            email.fail_silently = False
            email.send()
            print('Message sent successfully via email')
        except Exception as e:
            print(e)
        message = Message.objects.create(name=name, location=location, email=email, subject=subject, message=message)
        message.save()
        response = {
            'status': 'success',
            'message': 'Your message was sent successfully'
        }
    return JsonResponse(response, safe=False)