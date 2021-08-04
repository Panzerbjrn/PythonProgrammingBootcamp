'''
More String Functions
To solve this problem:
Your output must be exactly the same as you'll see below
1. Create a variable named samp_string and assign the value "  This is a very important string  "
2. Get rid of the extra whitespace and then provide the following output. You'll have to use
multiple functions, convert strings and more

Uppercase : THIS IS A VERY IMPORTANT STRING
Lowercase : this is a very important string
Words
This
is
a
very
important
string
How many ts? 3
String Index : 25
Replace very : This is kind of important string
is "z" a letter of number : True
'''
# Create samp_string variable
samp_string = "  This is a very important string  "

# remove white space
samp_string = samp_string.lstrip()
samp_string = samp_string.rstrip()

# Uppercase
print("Uppercase :", samp_string.upper())

# Lowercase
print("Lowercase :", samp_string.lower())

# print Words for above the breakout loop
print("Words")
# turn each word of the string into a list element
samp_string_list = samp_string.split()
# print each word individually using for loop
for i in samp_string_list:
    print(i)

# count ts
print("How many ts?", samp_string.count("t"))

# string index (length)
print("String Index :", samp_string.find("string"))

# replace very with kind of
print("Replace very :", samp_string.replace("very", "kind of"))

# checks if z is alphanumberic
print('Is "z" a letter or number :', "z".isalnum())

# checks if z is a letter
print('Is "z" a letter :', "z".isalpha())

# checks if z is a number
print('Is "z" a number :', "z".isdigit())

# checks if z is a space
print('Is "z" a space :', "z".isspace())