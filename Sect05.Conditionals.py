'''
import math
num_1, num_2 = input('Enter two numbers to multiply ').split()

print(num_1,"*",num_2,"=",(int(num_1)*int(num_2)))

age = int(input("Enter your age"))

if (age <= 5):
    print("Go To Kindergarten")
elif (age == 6):
    print("Go To Grade 1")
elif (age == 7):
    print("Go To Grade 1")
elif (age == 8):
    print("Go To Grade 1")
elif (age == 9):
    print("Go To Grade 1")
elif (age == 10):
    print("Go To Grade 1")
elif (age == 11):
    print("Go To Grade 1")
elif (age == 12):
    print("Go To Grade 1")
elif (age == 13):
    print("Go To Grade 1")
elif (age == 14):
    print("Go To Grade 1")
elif (age == 15):
    print("Go To Grade 1")
elif (age == 16):
    print("Go To Grade 1")
elif (age >= 17) and (age <= 64):
    print("Go To College")
elif (age >= 65):
    print("retire")
else:
    print("Bruh?")
'''

age = int(input("Enter your age"))
Can_Vote = True if (age >= 18) else False
print("Can vote: ", Can_Vote)