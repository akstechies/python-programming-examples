#===========

# * n! = n * (n-1) * (n-2) *........1  
# * 4! = 4x3x2x1 = 24 

n = 10
      
for i in range(1, n):
    n *= i               # * n * 1 = 10, n * 2 = 20, n * 3 = 60 ..... n * 9
print(n)

# =============

num = 10
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
    for i in range(1,num + 1): 
       factorial = factorial*i          # * 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6 ..... fact * 10 
print("The factorial of",num,"is",factorial)       

# =============

# TODO: Using Recursion

def fact(n):
   return 1 if (n==1 or n==0) else n * fact(n - 1)

def fact2(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

print(fact(10))
print("fact2", fact2(10))

# =============
#TODO: Using built-in function - factorial()

import math

factNum = 10
factorialValue = math.factorial(factNum)

print(factorialValue)