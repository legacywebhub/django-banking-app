from django.test import TestCase
import random

# Create your tests here.
def generateVirtualCardNumber():
    num = ''
    for x in range(20):
        if x % 5 == 0:
            i = " "
        else:
            i = str(random.randint(0, 9))
        num += i
    return num
print(generateVirtualCardNumber())