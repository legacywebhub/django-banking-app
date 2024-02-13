from django.contrib import admin
from.models import *
from django.utils.html import format_html
from django.urls import reverse


class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'site_domain', 'email', 'interest_rate', 'interest_button']

    def interest_button(self, obj):
        topup_url = reverse('banking:topup_interest')
        button = format_html(f'<a href="{topup_url}" class="btn btn-primary">Top Up Interest</a>')
        return button
    interest_button.short_description = 'Actions'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'amount', 'method', 'purpose', 'transact_proof', 'status', 'action_buttons')
    list_filter = ('status', 'method', 'purpose', 'timestamp',)
    list_per_page = 20

    def transact_proof(self, obj):
        if obj.proof:
            image = format_html(f'<a href="/media/{obj.proof}" target="_blank"><img src="/media/{obj.proof}" style="width:70px;" /></a>') 
        else:
            image = " "
        return image
    transact_proof.short_description = "Proof"

    def action_buttons(self, obj):
        if obj.status == 'pending':
            approve_url = reverse('banking:approve_payment', args=[obj.id])
            decline_url = reverse('banking:decline_payment', args=[obj.id])
            button = format_html(f'<a href="{approve_url}" class="btn btn-primary">Approve</a>&nbsp;&nbsp;<a href="{decline_url}" class="btn btn-danger">Decline</a>')
        else:
            button = '-'
        return button
    action_buttons.short_description = "Actions"


class KYCAdmin(admin.ModelAdmin):
    list_display = ['user', 'id_type', 'user_passport', 'user_id_upload', 'status', 'action_buttons']
    list_filter = ['status',]

    def user_passport(self, obj):
        if obj.passport:
            image = format_html(f'<a href="/media/{obj.passport}" target="_blank"><img src="/media/{obj.passport}" style="width:70px;" /></a>') 
        else:
            image = " "
        return image
    user_passport.short_description = "Passport"

    def user_id_upload(self, obj):
        if obj.id_upload:
            image = format_html(f'<a href="/media/{obj.id_upload}" target="_blank"><img src="/media/{obj.id_upload}" style="width:70px;" /></a>') 
        else:
            image = " "
        return image
    user_id_upload.short_description = "ID Photo"

    def action_buttons(self, obj):
        if obj.status == 'pending':
            approve_url = reverse('banking:approve_kyc', args=[obj.id])
            decline_url = reverse('banking:decline_kyc', args=[obj.id])
            button = format_html(f'<a href="{approve_url}" class="btn btn-primary">Approve</a>&nbsp;&nbsp;<a href="{decline_url}" class="btn btn-danger">Decline</a>')
        else:
            button = '-'
        return button
    action_buttons.short_description = "Actions"


class LoanAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'loan_amount', 'status', 'action_buttons')
    list_display_links = ('date',)
    list_filter = ('status', 'date', 'approved_date', 'end_date')
    list_per_page = 20

    def loan_amount(self, obj):
        return f'{obj.user.currency}{obj.amount}'

    def action_buttons(self, obj):
        if obj.status == 'pending':
            approve_url = reverse('banking:approve_loan', args=[obj.id])
            decline_url = reverse('banking:decline_loan', args=[obj.id])
            button = format_html(f'<a href="{approve_url}" class="btn btn-primary">Approve</a>&nbsp;&nbsp;<a href="{decline_url}" class="btn btn-danger">Decline</a>')
        else:
            button = '-'
        return button
    action_buttons.short_description = "Actions"


class UserAdmin(admin.ModelAdmin):
    exclude = ('theme',)
    list_display = ( 'full_name', 'email', 'account_number', 'user_balance', 'user_overdraft')
    list_display_links = ('full_name', 'email')
    list_filter = ('first_name', 'last_name', 'email',)
    list_per_page = 20

    # Block user button
    def action_buttons(self, obj):
        if not obj.is_blocked:
            url = reverse('mining:block_user', args=[obj.id])
            return format_html('<a href="{}" class="btn btn-danger text-light">Block</a>', url)
        else:
            url = reverse('mining:unblock_user', args=[obj.id])
            return format_html('<a href="{}" class="btn btn-info text-light">Unblock</a>', url)
    action_buttons.short_description = 'Actions'

    # Render filtered options only after 3 characters were entered
    filter_input_length = {
        "first_name": 3,
        "last_name": 3,
        "email": 3
    }


class VirtualCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_type', 'status',)
    list_per_page = 30

    # Card Actions
    def action_button(self, obj):
        if not obj.is_blocked:
            url = reverse('mining:block_user', args=[obj.id])
            return format_html('<a href="{}" class="btn btn-danger text-light">Activate</a>', url)
        else:
            url = reverse('mining:unblock_user', args=[obj.id])
            return format_html('<a href="{}" class="btn btn-info text-light">Nullify</a>', url)
    action_button.short_description = 'Actions'

    # Render filtered options only after 5 characters were entered
    filter_input_length = {
        "user": 5,
    }


# Register your models here.
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(KYC, KYCAdmin)
admin.site.register(Loan, LoanAdmin)
admin.site.register(Notification)
admin.site.register(Transaction)
admin.site.register(User, UserAdmin)
admin.site.register(VirtualCard, VirtualCardAdmin)
