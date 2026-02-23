# strings are immutable
name = "John"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-1])

# string slicing
print(name[0:2])
print(name[1:3])
print(name[2:4])
print(name[3:5])

course = "Complete Python Bootcamp"
print(course[0:8])
print(course[9:15])
print(course[16:24])

# print length of string
print(len(course))

# string concatenation
first_name = "John"
last_name = "Doe"
print(first_name + " " + last_name)

# string methods
print(first_name.upper())  # converts to uppercase
print(last_name.lower())  # converts to lowercase
print(first_name.title())  # capitalizes first letter of each word
print(first_name.strip())  # removes whitespace
print(first_name.rstrip())  # removes whitespace from right
print(first_name.lstrip())  # removes whitespace from left
# replaces a substring with another substring
print(first_name.replace("John", "Jane"))
print(first_name.find("John"))  # finds the index of a substring
print(first_name.index("John"))  # finds the index of a substring
print("Doe" in first_name)  # checks if a substring is in a string
print("Doe" not in first_name)  # checks if a substring is not in a string
# counts the number of occurrences of a substring
print(first_name.count("John"))
# checks if a string starts with a specific substring
print(first_name.startswith("John"))
# checks if a string ends with a specific substring
print(last_name.endswith("Doe"))
print(first_name.join(last_name))  # joins two strings
print(first_name.split())  # splits a string into a list
