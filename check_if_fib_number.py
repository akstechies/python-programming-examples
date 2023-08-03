def is_perfect_square(num):
    root = int(num ** 0.5)
    return root * root == num

def is_fibonacci_number(n):
    if n <= 0:
        return False

    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Test the function
# number_to_check = int(input("Enter a number to check if it's in the Fibonacci series: "))
number_to_check = 5
if is_fibonacci_number(number_to_check):
    print(f"{number_to_check} is a Fibonacci number.")
else:
    print(f"{number_to_check} is not a Fibonacci number.")