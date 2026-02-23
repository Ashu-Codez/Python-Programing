high_income = false

good_credit = True
student = False

# becasue of short circuiting it will not check the second condition if the first condition is false it will always return false
if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not Eligible")


# becasue of short circuiting it will check atlease one condition is true
if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")
