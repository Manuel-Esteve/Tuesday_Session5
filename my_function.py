def greet():
    """
    A simple function that prints hello
    :return: None
    """
    print("Hello!")

greet()
greet()

def greet2(name):
    """
    A more advanced greet function
    :param name:
    :return:
    """
    print(f"Hello {name}")

greet2("James")
greet2("Bob")

def average(a, b):
    """
    Average the 2 numbers
    :param a: first number
    :param b: second number
    :return: float, average of a and b
    """
    average = (a + b)/2
    return average # this is how a function returns a value

print(average(10,20))

def divide(x, y):
    """
    Divide x by y
    :param x: first number
    :param y: second number
    :return: float, the division result
    """
    if y == 0:
        return None
    return x / y

print(divide(10,20))
print(divide(10,0))
print(divide(10,1))


def bond(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name}, {last_name}"

def introduce(name):
    print(f"The name is: {name}")

print(bond("James", "Smith"))
introduce(bond("James", "Smith"))