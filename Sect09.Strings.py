SampleString = "This is a very long string"
'''
print(type(3))
print(type(3.14))
print(type(3.99))
print(type('3.99'))
print("Length of String :",len(SampleString))
print(SampleString[0])
print(SampleString[1])
print(SampleString[2])
print(SampleString[3])
print(SampleString[4])
print(SampleString[5])
print(SampleString[6:9])
print(SampleString[9:])
print("Every other character : ", SampleString[0:-1:2])
print("Every other character : ", SampleString[1:-1:2])
print("Reverse: ", SampleString[::-1])
#print("Every other character : ", SampleString[0:-1:-1])
#print("Every other character : ", SampleString[1:-1:-1])
for char in SampleString:
    print(char)

for i in range(0, len(SampleString)-1, 2):
    print(SampleString[i] + SampleString[i+1])

print("A =", ord("A"))
print("a =", ord("a"))
print("æ =", ord("æ"))
print("ø =", ord("æ"))
print("65 = ", chr(65))

for i in range(200, 299):
    print(i, " = ", chr(i))
'''
StrVar = "CAT"
StrOrd = ""
for char in StrVar:
    print(ord(char))
    StrOrd += str(ord(char))

for char in StrOrd:
    print(char)
