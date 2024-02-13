from django.urls import path
from . import views
from .views import PasswordsChangeView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

app_name='banking'
urlpatterns = [
    # Page urls and paths
    path('sitemap.xml/', sitemap, {'sitemaps':sitemaps}),
    #path('', views.index, name='index'),


    # Auth urls

    # Dashboard and account pages
    path('account/', views.account, name='account'),
    path('account/fund-account/', views.fundAccount, name='fund_account'),
    path('account/payment/<str:id>/', views.payment, name='payment'),
    path('account/transactions/', views.transactions, name='transactions'),
    path('account/transaction/<str:id>/', views.viewTransaction, name='transaction'),
    path('account/credit-history/', views.creditHistory, name='credit_history'),
    path('account/debit-history/', views.debitHistory, name='debit_history'),
    path('account/transfer-history/', views.transferHistory, name='transfer_history'),
    path('account/loan-request/', views.loanRequest, name='loan_request'),
    path('account/loan/<str:id>', views.viewLoan, name='loan_detail'),
    path('account/loan-history/', views.loanHistory, name='loan_history'),
    path('account/inter-transfer/', views.internalTransfer, name='internal_transfer'),
    path('account/domestic-transfer/', views.domesticTransfer, name='domestic_transfer'),
    path('account/international-transfer/', views.internationalTransfer, name='international_transfer'),
    path('account/usdt-transfer/', views.usdtTransfer, name='usdt_transfer'),
    path('account/change-pin/', views.changeTransactionPin, name='change_pin'),
    path('account/virtual-card/', views.puchaseVirtualCard, name='virtual_card'),
    path('account/notifications/', views.notifications, name='notifications'),
    path('account/profile/', views.profile, name='profile'),
    path('account/logout/', views.logout, name='logout'),

    # Pseudo views

    path('process_theme/', views.processTheme, name='process_theme'),
    path('process_message/', views.processMessage, name='process_message'),
    path('process_registeration/', views.processRegisteration, name='process_registeration'),
    path('process_internal_transfer/', views.processInternalTransfer, name='process_internal_transfer'),
    path('block_user/<str:id>/', views.blockUser, name='block_user'),
    path('unblock_user/<str:id>/', views.unblockUser, name='unblock_user'),
    path('process_kyc/', views.processKYC, name='process_kyc'),
    path('approve_kyc/<str:id>/', views.approveKYC, name='approve_kyc'),
    path('decline_kyc/<str:id>/', views.declineKYC, name='decline_kyc'),
    path('approve_loan/<str:id>/', views.approveLoan, name='approve_loan'),
    path('decline_loan/<str:id>/', views.declineLoan, name='decline_loan'),
    path('approve_payment/<str:id>/', views.approvePayment, name='approve_payment'),
    path('decline_payment/<str:id>/', views.declinePayment, name='decline_payment'),
    path('process_payment/', views.processPayment, name='process_payment'),
    path('process_loan_request/', views.processLoanRequest, name='process_loan_request'),
    path('topup_interest/', views.topupInterest, name='topup_interest'),
    path('send_otp/<str:otp>/', views.sendOTP, name='send_otp'),
    path('change_pin/', views.changePin, name='change_pin'),
]