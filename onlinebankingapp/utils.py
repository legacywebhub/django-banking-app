import datetime, pytz, requests, random
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from decimal import Decimal



############# ACCOUNT UTILS #################
def generateAcountNumber():
    number = ''
    for x in range(10):
        i = str(random.randint(0, 9))
        number += i
    return number


def generateOTP():
    otp = ''
    for x in range(4):
        i = str(random.randint(0, 9))
        otp += i
    return otp


############# TRANSACTION UTILS #################
def generateSessionID():
    session_id = ''
    for x in range(24):
        i = str(random.randint(0, 9))
        session_id += i
    return session_id


def generateTransactionNumber():
    transac_num = ''
    for x in range(12):
        i = str(random.randint(0, 9))
        transac_num += i
    return transac_num


############# VIRTUAL CARD UTILS #################
def generateVirtualCardNumber():
    num = ''
    for x in range(20):
        if x % 5 == 0:
            i = " "
        else:
            i = str(random.randint(0, 9))
        num += i
    return num


def generateCVV():
    number = ''
    for x in range(3):
        i = str(random.randint(0, 9))
        number += i
    return number


############### FUNCTION UTILS ################
def authorizeUser(user):
    '''
    * Note that we can only use HttpResponseForbidden in views
    so we cant return or redirect forbidden users from here

    * Note also we cant use IPs to block users since one request user
    can possess up to 5 IPs which is not static (changes periodically)
    But just incase below is the code to get users IP adress
    # ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
    '''

    if user.is_authenticated and user.is_blocked:
        forbidden = True
    elif user.is_authenticated and not user.is_blocked:
        forbidden = False
    elif not user.is_authenticated:
        forbidden = False
    else:
        forbidden = False
    return forbidden


def fetchFinanceNews(url):
    try:
        # Make the API request using the GET method
        response = requests.get(url)

        # Check the status code of the response to ensure it was successful
        if response.status_code == 200:
            # Extract the JSON response content from the response object
            response = response.json()
            finance_news = []

            # We only want 3 random articles per page load
            # Generate 3 random numbers within 0 to 99
            random_numbers = random.sample(range(100), 3)

            # Loop through random numbers to select random news/articles
            for random_number in random_numbers:
                finance_news.append(response["articles"][random_number])

        else:
            finance_news = []
    except:
        finance_news = []
    return finance_news
