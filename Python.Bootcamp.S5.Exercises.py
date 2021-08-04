int_Age = int(input("What is your age "))
print("You are",int_Age,"Years old")

if (int_Age == 5):
    print("Go to Kindergarten")
elif (int_Age >= 6) and (int_Age <= 17):
    print("Go to school")
elif (int_Age >= 17):
    print("Go to College")