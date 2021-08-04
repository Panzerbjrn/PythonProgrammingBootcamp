TallnessofTree = int(input("How tall should the tree be? "))
HashVar = '#'
NumOfHashes = int(3)
#print(HashVar*NumOfHashes)
print(HashVar*TallnessofTree)
print("#")

TallnessCount = int(1)
print("TallnessCount is", TallnessCount)
print("TallnessofTree is", TallnessofTree)
while TallnessCount !> TallnessofTree:
    TallnessCount = TallnessCount + 1
    print("TallnessCount is", TallnessCount)
    print(TallnessCount)
    print(HashVar*TallnessCount)
    print(HashVar*TallnessofTree)
