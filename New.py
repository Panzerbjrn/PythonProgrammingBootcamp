#This is a comment.
"""
This is a
Multiline Comment
"""
print("Hello, World!")

if 5 > 2:
  print("Five is greater than two!")
  
if 5 > 2:
 print("Five is greater than two!")

X = 5
Y = "John"
Z = "5"
print(X)
print(X*2)
print(Y)
print(Z)
print(Z*2)
print(type(X))

x, y, z = "Orange", "Banana", "Cherry"
print(X)
print(y)
print(z)
print(type(X)) 

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print(type(X))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(x)
print(type(y))
print(type(z)) 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10)) 