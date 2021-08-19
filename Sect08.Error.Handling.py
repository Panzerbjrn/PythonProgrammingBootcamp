'''
while True:
    try:
        number = int(input("Please enter a number : "))
        break
    
    except ValueError:
        print("You didn't enter a number!")
    except:
        print("Unknown Error!!!")
        
print("You Entered : ", number)

SekritNumber = 8
Guess = int(input("Please guess a number 1-10 : "))
while SekritNumber != Guess:
    Guess = int(input("Please guess a number 1-10 : "))

SekritNumber = 8
while True:
    Guess = int(input("Please guess a number 1-10 : "))
    if Guess == SekritNumber:
        print("Well Done!")
        break

from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")
'''
from decimal import *
sum_1 = Decimal(0)

'''


'''
