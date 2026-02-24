
# function
# def mean defination
# def mean calling

def greet():
    print("Hello World")


greet()

# function with parameter and argument


def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


greet("John", "Doe")  # if you dont give any of the  argument it will give error

# function returning value


def name(name):
    return f"Hello {name}"


message = name("John")
print(message)


# in python All function return bydefault None value
# if you dont return any value it will return None


def add(a, b):
    print(a + b)


print(add(1, 2))


# keyword argument

def increment(number, by):
    return number + by


print(increment(number=1, by=2))

# default argument


# every default argument must after the required argument that means in the end
def decrement(number, by=1):
    return number - by


# but if you give the second argument it will use that instead of default value
print(decrement(number=1))


# *args


def multipleNum(*args):

    total = 1
    for num in args:
        total += num
    return total


print(multipleNum(1, 2, 3, 4, 5))  # it will print tuple

# a tuple is similar to list but it is immutable , we can't change add new element in tuple
