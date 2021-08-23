'''
num_3 = int(5)
num_4 = int(4)


def mult_divide(num_1, num_2):
    return (num_1 * num_2), (num_1 / num_2)

mult, divide = mult_divide(num_3, num_4)

print(num_3, " * ", num_4, " = ", mult)
print(num_3, " / ", num_4, " = ", divide)

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes

max_num_to_check = int(input("Enter Number to check: "))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)

def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


print("Sum : ", sum_all(1, 2, 3, 4, 5))

'''
import math

def Get-Area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Enter circle or rectangle")

def rectangle_area()
    

def circle_area()
