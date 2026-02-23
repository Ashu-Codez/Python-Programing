# x = input("x : ")  # when give it a value it will be string
# y = x + 1  # it will give error because x is string and 1 is integer

# type conversion
x = input("x : ")
x = int(x)  # it will convert x to integer
y = x + 1  # it will not give error because x is integer and 1 is integer
print(f"x : {x}, y : {y}")

# type casting
x = float(x)  # it will convert x to float
y = x + 1  # it will not give error because x is float and 1 is integer
print(f"x : {x}, y : {y}")

x = str(x)  # it will convert x to string
# y = x + 1  # it will give error because x is string and 1 is integer
# print(f"x : {x}, y : {y}")

x = bool(x)  # it will convert x to boolean
# in python we have a concept of truthy and falsy values
# truthy values - True, 1, 1.0, "hello", "0", "[]", "{}", "()"
# falsy values - False, 0, "" empty string, [] empty list, {} empty dictionary, () empty tuple
print(bool("hello"))
print(bool(""))
print(bool(0))
print(bool(1))
print(bool(1.0))
print(bool("[]"))
print(bool("{}"))
print(bool("()"))

x = list(x)  # it will convert x to list
# what is list - list is a collection of items in a single variable example - [1, 2, 3]
y = x + 1  # it will give error because x is list and 1 is integer
print(f"x : {x}, y : {y}")

x = tuple(x)  # it will convert x to tuple
# what is tuple - tuple is a collection of items in a single variable example - (1, 2, 3)


x = set(x)  # it will convert x to set
y = x + 1  # it will not give error because x is set and 1 is integer
print(f"x : {x}, y : {y}")

x = dict(x)  # it will convert x to dict
y = x + 1  # it will not give error because x is dict and 1 is integer
print(f"x : {x}, y : {y}")

x = complex(x)  # it will convert x to complex
y = x + 1  # it will not give error because x is complex and 1 is integer
print(f"x : {x}, y : {y}")
