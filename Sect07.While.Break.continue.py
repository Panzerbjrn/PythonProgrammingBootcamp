'''
import random

rand_num = random.randrange(1, 51)
i = 1
while i != rand_num:
    i += 1
print("The Rand num is : ", rand_num)

i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd :", i)
    i += 1

    #
   ###
  #####
 #######
#########
    #
'''
    
Rows = int(input('How many rows should the tree have? '))
i = 1
Hashes = 1
while i <= Rows:
    Indent = Rows - i
    #print("indent is: ", Indent)
    print(" "*Indent,"#"*Hashes)
    i+= 1
    Hashes = Hashes + 2
StumpIndent = Rows - 1
print(" "*(Rows - 1),"#")
#print(i)
#print(i)

'''

'''
