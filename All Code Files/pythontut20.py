class Sum:
    # You use the static method decorator to define that a
    # method is static
    @staticmethod
    def get_sum(*args):
        sum_1 = 0
        for i in args:
            sum_1 += i
        return sum_1

class Dog:
    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))

def main():
    # Call a static method by proceeding it with its class
    # name
    print("Sum :", Sum.get_sum(1, 2, 3, 4, 5))
    spot = Dog("Spot")
    doug = Dog("Doug")
    spot.get_num_of_dogs()


main()