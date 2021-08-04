'''
1
Your code should receive a uppercase string and then hide it’s meaning by turning it into a
string of unicodes. Then it should translate the unicodes back into the original message.
'''
'''
# Take in a UPPERCASE word
UCString = str(input("Please enter a word in all UPPERCASE letters: "))
# Set the Unicode string to nothing at first
UNIString = str("")
# Convert string to unicode
for i in UCString:
	UNIString += str(ord(i))
# Print the Unicode String as unicode
print("Unicode String is:", UNIString)
# Sets the UPPEPRCASE word to nothing in order to reset it from the unicode
UCString = str("")
# Loops the Unicode back into the UPPERCASE word string 1 letter at a time
# Needs to pull in 2 at a time in order to get both digits of the unicode (65 - 90 for A - Z)
for i in range(0, len(UNIString) - 1, 2):
    # char will be 2 digits
    char_UNICODE = UNIString[i] + UNIString[i+1]
    # Adds each char individually based on the 2 digit unicode
    UCString += chr(int(char_UNICODE))
# prints the original UCString
print("The original UPPERCASE word is:", UCString)
'''

'''
2
Your code should receive a uppercase string and then hide it’s meaning by turning it into a
string of unicodes. Then it should translate the unicodes back into the original message.

Make the above work with upper and lowercase letters by changing 2 lines of code.
'''

# Take in a word
UCString = str(input("Please enter a word: "))
# Set the Unicode string to nothing at first
UNIString = str("")
# Convert string to unicode
# We are going to subtract 23 from the unicode to handle the lowercase letters that
# turn the ord into a triple digit (i.e. a - z is 97 - 122, hence d-z is over 100)
for i in UCString:
	UNIString += str(ord(i) - 23)
# Print the Unicode String as unicode
print("Unicode String is:", UNIString)
print("Note: All double digit values are 23 less than the real unicode values")
# Sets the UPPEPRCASE word to nothing in order to reset it from the unicode
UCString = str("")
# Loops the Unicode back into the UPPERCASE word string 1 letter at a time
# Needs to pull in 2 at a time in order to get both digits of the unicode (65 - 90 for A - Z)
for i in range(0, len(UNIString) - 1, 2):
    # char will be 2 digits
    char_UNICODE = UNIString[i] + UNIString[i+1]
    # Adds each char individually based on the 2 digit unicode
    # We add the 23 back to the unicode value because we removed it earlier to
    # make the char_UNICODE only pull 2 digit values
    UCString += chr(int(char_UNICODE) + 23)
# prints the original UCString
print("The original word:", UCString)