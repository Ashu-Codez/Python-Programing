# range is complex type
# range is iterable
# it returns sequence of numbers range objects

# range(start, stop, step)
for i in range(10):
    print(i)

# range(10) is same as range(0, 10)

for x in range(0, 10):
    print(x)

# string is iterable

for x in "Python":
    print(x)


# list is iterable

for x in [1, 2, 3, 4, 5]:
    print(x)

# adding element in list in last
list = [1, 2, 3, 4, 5]

for x in list:
    print(x)


list.append(6)

# adding element in list in first
list.insert(0, 0)  # insert(index, element)


# tuple is iterable
# tuple is immutable
for x in (1, 2, 3, 4, 5):  # paranthesis is optional
    print(x)

# set is iterable
# set has unique values
# there is no order in set , there is no indexing in set
for x in {1, 2, 3, 5, 5}:  # set has unique values
    print(x)  # 5 will be printed only once


# custom object is iterable

for item in shopping_cart:
    print(item)


# dictionary is iterable
# dictionary has key-value pairs
# dictionary is ordered
# dictionary is mutable
# dictionary is indexed
for x in {"name": "John", "age": 30, "city": "New York"}:
    print(x)

# we can add element in dictionary
dict = {"name": "John", "age": 30, "city": "New York"}
dict["country"] = "USA"
print(dict)

# we can remove element from dictionary
dict.pop("country")
print(dict)

# we can update element in dictionary
dict["age"] = 31
print(dict)

# we can delete element from dictionary
del dict["age"]
print(dict)

# we can clear the dictionary
dict.clear()
print(dict)

# we can iterate over the values of the dictionary
for x in {"name": "John", "age": 30, "city": "New York"}.values():
    print(x)

# we can iterate over the keys of the dictionary
for x in {"name": "John", "age": 30, "city": "New York"}.keys():
    print(x)

# we can iterate over the items of the dictionary
for x in {"name": "John", "age": 30, "city": "New York"}.items():
    print(x)
