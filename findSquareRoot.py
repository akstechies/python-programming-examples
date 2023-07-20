#Python Program to Find the Square Root

# =========================
# We kknow that square root of a number is num^1/2
# In python we can give power using ** => num ** 0.5

# Lets first take input from user
# num = int( input("Enter the num: ") )

num = 8

sqrt = num ** 0.5

print(f"sqrt is {sqrt}")

#output
# Enter the num: 4
# sqrt is 2.0

# Enter the num: 8
# sqrt is 2.8284271247461903

print("=========================")
# =========================

# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print(num_sqrt.real)
print(num_sqrt.imag)
print(num_sqrt)