temperture = 15

if temperture > 30:  # colon is very important
    # This block is indented with 4 spaces
    print("It is hot")
    print("Drink water")
elif temperture > 20:
    print("It is warm")
    print("Drink water")
else:
    print("It is cold")
    print("Drink water")
# this is not indented so it will not execute whether the condition is true or false
print("Done")
