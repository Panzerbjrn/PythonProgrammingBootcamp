'''
1. Receive a message and then encrypt iy by shifting the
characters by a requested amount to the right

A becomes D, B becomes E for example. also decrypt the
message back again

HINTS
1. A-Z have the numbers 65-90 in unicode
2. a-z have the numbers 97-122
3. You get the unicode of a character with ord(yourLetter)
4. You convert from unicode with chr(yourNumber)
5. Use isupper() to decide which unicodes to work with
6. Add the key (number of characters to shift) and
if bigger or smaller then the unicode for A, Z, a,
or z increase or decrease by 26
'''

# Message to encrypt
message = input("Enter message to Encrypt: ")
# Sets the encrypted message to nothing for now
encryptedmessage = ""
# sets to 0 so it asks below
shiftkey = 0
# Checks to make sure that the shiftkey is between 1 and 26
while shiftkey < 1 or shiftkey > 26:
    shiftkey = input("Enter amount of letters to shift by (1 through 26): ")
    shiftkey = int(shiftkey)
# for loop to check each index of the message
for char in message:
    # checks if the index is a letter or number
    if char.isalpha():
        # shifts the unicode value to the right (positive) by the key amount
        char_code = ord(char) + shiftkey
        # Checks if the indexes letter is uppercase
        # the following if statements make sure that the letter stays in
        # the uppercase range of 65-90
        if char.isupper():
            # if the unicode value for char_code is greater than the Z unicode
            # it shifts it back 26 to get it into the uppercase range 65-90
            if char_code > ord("Z"):
                char_code -= 26
            # if the unicode value for char_code is less than the A unicode
            # it shifts it forward 26 to get it into the uppercase range 65-90
            elif char_code < ord("A"):
                char_code += 26
        # else in this case is only letters that are lowercase per previous
        # criteria that we set with isalpha and already having checked .isupper()
        else:
            # if the unicode value for char_code is greater than the z unicode
            # it shifts it back 26 to get it into the lowercase range 97-122
            if char_code > ord("z"):
                char_code -= 26
            # if the unicode value for char_code is less than the a unicode
            # it shifts it forward 26 to get it into the lowercase range 97-122
            elif char_code < ord("a"):
                char_code += 26
        # At this point it builds the encrypted message letter by letter
        # since it knows if they are upper or lower case letters and
        # it shifts them properly to ensure they stay that way
        # the next else handles things that aren't letters
        encryptedmessage += chr(char_code)
    # this else handles all non-letters
    else:
        # there is no modifications necessary for spaces, numbers and non-alphanumerics
        # they simply need to be added character by character
        encryptedmessage += char
# prints the final encrypted message
print ("Encrypted Message: ", encryptedmessage)

# Need to set the message back to blank, otherwise when adding characters it will add
# to the original message variable
message = ""
# for loop to check each index of the decrypted message
for char in encryptedmessage:
    # checks if the index is a letter
    if char.isalpha():
        # shifts the unicode value to the left (negative) by the key amount
        char_code = ord(char) - shiftkey
        # Checks if the indexes letter is uppercase
        # the following if statements make sure that the letter stays in
        # the uppercase range of 65-90
        if char.isupper():
            # if the unicode value for char_code is greater than the Z unicode
            # it shifts it back 26 to get it into the uppercase range 65-90
            if char_code > ord("Z"):
                char_code -= 26
            # if the unicode value for char_code is less than the A unicode
            # it shifts it forward 26 to get it into the uppercase range 65-90
            elif char_code < ord("A"):
                char_code += 26
        # else in this case is only letters that are lowercase per previous
        # criteria that we set with isalpha and already having checked .isupper()
        else:
            # if the unicode value for char_code is greater than the z unicode
            # it shifts it back 26 to get it into the lowercase range 97-122
            if char_code > ord("z"):
                char_code -= 26
            # if the unicode value for char_code is less than the a unicode
            # it shifts it forward 26 to get it into the lowercase range 97-122
            elif char_code < ord("a"):
                char_code += 26
        # At this point is builds the decrypted message letter by letter
        # since it knows if they are upper or lower case letters and
        # it shifts them properly to ensure they stay that way
        # the next else handles things that aren't letters
        message += chr(char_code)
    # this else handles all non-letters
    else:
        # there is no modifications necessary for spaces, numbers and non-alphanumerics
        # they simply need to be added character by character
        message += char
# prints the shiftkey original message after being decrypted from the original message
print("Your Shift Key is: ", shiftkey)
print("Decrypted Message: ", message)