'''
Acronym Generator
Note: I did it the same exact way that Derek did, great minds think alike lol
'''

# Take in string
acrstring = input("Enter word to make an acronym of: ")
# Uppercase all words
acrstring = acrstring.upper()
# Split words into a list
acrstring = acrstring.split()
# Create a loop where i is the element of the list
for i in acrstring:
    # prints the first index of element i, no space between them
    print(i[0], end="")

