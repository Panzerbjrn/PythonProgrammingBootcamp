# VIDEO 11 : LISTS

# With lists we can refer to groups of data with 1 name
# Each item in the list corresponds to a number (index) just like how people have identification numbers
# By default the 1st item in a list has the index 0.

# Ex. [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]
#  
# Python lists can grow in size and can contain data of any type
# An awesome thing about lists is that you can use many of the same functions with them that you used with strings

rand_list = ["string", 1.234, 28]

# Create a list with range
one_to_ten = list(range(10))

# Combine lists
rand_list = rand_list + one_to_ten

# Get the 1st item with an index
print(rand_list[0])

# Get the length
print("List Length :", len(rand_list))

# Slice a list to get 1st 3 items
first3 = rand_list[0:3]

# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
print(first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")

# Python Problem for you to Solve

# For this problem generate a random list of 5 values between 1 and 9
import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))

# Bubble Sort

# The Bubble sort is a way to sort a list. It works this way :
# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[Index] > list[Index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1

# Create the value that will decrement for the outer loop
# Its value is the last index in the list
i = len(num_list) - 1
while i > 1:
    j = 0

    while j < i:
        # Tracks the comparison of index values
        print("\nIs {} > {}".format(num_list[j], num_list[j+1]))
        print()

        # If the value on the left is bigger switch values
        if num_list[j] > num_list[j+1]:
            print("Switch")

            temp = num_list[j]
            num_list[j] = num_list[j + 1]
            num_list[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        # Track changes to the list
        for k in num_list:
            print(k, end=", ")
        print()
    print("END OF ROUND")

    i -= 1

for k in num_list:
    print(k, end=", ")
print()

# More List Functions

import random
num_list = []
for i in range(5):
    num_list.append(random.randrange(1, 9))

# Sort a list
num_list.sort()

# Reverse a list
num_list.reverse()
for k in num_list:
    print(k, end=", ")
print()

# Insert value at index insert(index, value)
num_list.insert(5, 10)

# Delete first occurrence of value
num_list.remove(10)

for k in num_list:
    print(k, end=", ")
print()

# Remove item at index
num_list.pop(2)

for k in num_list:
    print(k, end=", ")
print()





