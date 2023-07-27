n = 10
fib = 1
count = 0

a = 0
b = 1
for i in range(n):
    print(a)            # a:0;    a:1;       a:2  
    c = a+b             #c=0+1=1; c= 1+1=2;  # Calculate the sum of 'a' and 'b' and store it in a temporary variable 'temp_sum'
    a = b               #a=1    ; a=1;       # Assign the current value of 'b' to 'a'    
    b = c               #b=1    ; b=2;       # Assign the calculated value (stored in 'temp_sum') to 'b'

""" # Before the assignment
# a -> old value of a
# b -> old value of b

# Evaluate the right-hand side
temp_sum = a + b

# Perform the assignments
a = b
b = temp_sum

# After the assignment
# a -> old value of b
# b -> temp_sum (which is the sum of old values of a and b) """