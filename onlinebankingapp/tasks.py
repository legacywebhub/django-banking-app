from . import models
import datetime, pytz, requests, random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from decimal import Decimal



# Function to perform account operations and create notification
def updateAccount(user, account, action, amount, message):
    if account == 'balance':
        if action == "credit":
            # Adding to user balance
            user.balance += amount
            # Creating notification
            notification = models.Notification.objects.create(
                user=user, 
                message=message
            )
            notification.save()
        elif action == "debit":
            if amount <= user.total_balance:
                user.balance -= amount
                # Creating notification
                notification = models.Notification.objects.create(
                    user=user, 
                    message=message
                )
                notification.save()
    elif account == 'overdraft':
        if action == "credit":
            # Adding to user overdraft
            user.overdraft += amount
            # Creating notification
            notification = models.Notification.objects.create(
                user=user, 
                message=message
            )
            notification.save()
        elif action == "debit":
            if amount <= user.overdraft:
                user.overdraft -= amount
                # Creating notification
                notification = Notification.objects.create(
                    user=user, 
                    message=message
                )
                notification.save()
    user.save()


# Function to perform internal transfers
def performInternalTransfer(sender, account, receiver_account_number, amount, remark):
    amount = Decimal(amount)

    if models.User.objects.filter(account_number=receiver_account_number).exists():
        receiver = models.User.objects.get(account_number=receiver_account_number)
        if sender.balance >= amount:
            if receiver.currency == sender.currency:
                # generating customers notifications
                sender_message = f'Your account was debited of ${amount}'
                receiver_message = f'Your account was credited with ${amount} from {sender.full_name}'
                # debit sender if account balance is equal or more than amount
                updateAccount(sender, account, "debit", amount, sender_message)
                # credit receiver
                updateAccount(receiver, account, "credit", amount, receiver_message)
                # creating transaction record
                transaction = models.Transaction.objects.create(
                    from_user=sender,
                    to_user=receiver,
                    transaction_type='transfer',
                    amount=amount,
                    remark=remark,
                    status='successful'
                )
                transaction.save()
                return "Transfer successful"
            else:
                amount = convertCurrency(sender.currency, receiver.currency, amount)

                # generating customers notifications
                sender_message = f'Your account was debited of ${amount}'
                receiver_message = f'Your account was credited with ${amount} from {sender.full_name}'
                # debit sender if account balance is equal or more than amount
                updateAccount(sender, "debit", amount, sender_message)
                # credit receiver
                updateAccount(receiver, "credit", amount, receiver_message)
                # creating transaction record
                transaction = models.Transaction.objects.create(
                    from_user=sender,
                    to_user=receiver,
                    transaction_type='transfer',
                    amount=amount,
                    remark=remark,
                    status='successful'
                )
                transaction.save()
                return "Transfer successful"
        else:
            return "Insufficient funds"
    else:
        return "Invalid account number"


# Function to check card expiry
def checkCardExpiry(user):
    today = datetime.datetime.now(tz=pytz.UTC).date()
    card = models.VirtualCard.get(user=user)
    # Here we trying to nullify the card if expired
    if today >=  card.expiry_date:
        card.status = 'null'
        card.card_type = None
        card.card_number = None
        card.approved_date = None
        card.expiry_date = None
        card.cvv = None
        card.save()


# Function to delete old notifications
def deleteOldNotifications(user):
    notifications = models.Notification.objects.filter(user=user)
    today = datetime.datetime.now(tz=pytz.UTC)

    for notification in notifications:
        # Getting number of days the notification has lasted
        notification_period = (today - notification.date).days
        #print(f'notification date: {notification.date} notification period: {notification_period}')
        if notification_period >= 3:
            notification.delete()