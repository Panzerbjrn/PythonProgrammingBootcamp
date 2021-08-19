'''
for i in (2,4,5,8):
    print("i =", i)
print(" ")
for i in range(2, 8):
    print("i =", i)
'''
import math
investment, interest = input('Enter Investment amount and expected interest rate: ').split()
investment = int(investment)
interest = int(interest)
interest = interest / 100
for i in range(10):
    investment = investment + (investment * interest)

print("Investment after 10 years is: {:.2f}".format(investment))

'''
'''

