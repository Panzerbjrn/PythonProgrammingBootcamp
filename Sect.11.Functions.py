'''
def func_name(x, y, z):



def add_numbers(x, y, z):


def change_name():
	return "Mark"

def get_sum(num_1, num_2):
	return num_1 + num_2
def is_float(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print(is_float("3"))
'''

def solve_eq(equation):
    x, add, num_1, equal, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)
    return "x = " +str(num_2 - num_1)

print(solve_eq("x + 6 = 9"))