# while loop - it is used to execute a block of statements repeatedly until a given condition is true

x = 3

while x < 10:
    print(x)
    x += 1

command = ""
while command.lower() != "quit":
    command = input("Enter a command: ")
    print("Echo", command)

# while condition:

#     statements

# infinite loop
# while True:
#     print("Hello")

# # break statement
# while True:
#     print("Hello")
#     break

command = ""
while True:
    command = input("Enter a command: ")
    print("Echo", command)
    if command.lower() == "quit":
        break

# # continue statement
# while True:
#     print("Hello")
#     continue
