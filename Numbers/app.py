import math
x = 10  # int number
a = 10.5  # float number
a = 2 + 3j  # complex number
y = 20


# augmented assignment operators
x = x + y
x += y  # x = x + y
x -= y  # x = x - y
x *= y  # x = x * y
x /= y  # x = x / y
x %= y  # x = x % y
x **= y  # x = x ** y
x //= y  # x = x // y

print(x + y)    # addition
print(x - y)    # subtraction
print(x * y)    # multiplication
print(x / y)    # division
print(x % y)    # modulo
print(x ** y)   # exponentiation
print(x // y)   # floor division  it gives you integer value
print(x == y)   # equality
print(x != y)   # inequality
print(x > y)    # greater than
print(x < y)    # less than
print(x >= y)   # greater than or equal to
print(x <= y)   # less than or equal to
print(x & y)    # bitwise AND
print(x | y)    # bitwise OR
print(x ^ y)    # bitwise XOR
print(x << y)   # bitwise left shift
print(x >> y)   # bitwise right shift


# working with numbers
x = 2.99
print(round(x))  # it rounds to the nearest integer
print(abs(x))  # it gives the absolute value turn negative number into positive
print(int(x))  # it gives the integer value
print(float(x))  # it gives the float value
print(complex(x))  # it gives the complex value
print(type(x))  # it gives the type of the value

# working with math module

print(math.ceil(x))  # it rounds to the nearest integer
print(math.floor(x))  # it rounds to the nearest integer
print(math.sqrt(x))  # it gives the square root
print(math.pow(x, y))  # it gives the power
print(math.factorial(x))  # it gives the factorial
print(math.gcd(x, y))  # it gives the greatest common divisor
print(math.lcm(x, y))  # it gives the least common multiple
print(math.pi)  # it gives the value of pi
print(math.e)  # it gives the value of e
print(math.inf)  # it gives the value of infinity
print(math.nan)  # it gives the value of not a number
