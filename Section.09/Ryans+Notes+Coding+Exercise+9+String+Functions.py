'''
String Functions
To solve this problem:
Your output must be exactly the same as you'll find below
1. Create a string named samp_string and assign the following "This is a very important string"
2. Output the following vased on this sample string
Length : 31
Last Character : g
1st 4 Characters : This
Reverse : gnirts tnatropmi yrev a si sihT
'''
# Sets the string as described in problem statement
samp_string = "This is a very important string"
# use len(variable) command to get string length
print("Length :", len(samp_string))
# use the last index [-1] command to get the last character
print("Last Character :", samp_string[-1])
# use the ranged index [#1:#2] command to get the 1st to 4th characters (0:4)
print("1st 4 Characters :", samp_string[0:4])
# use the reverse index [::-1] command to get the string in reverse
print("Reverse :", samp_string[::-1])