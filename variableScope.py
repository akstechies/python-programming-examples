# Global scope variable
global_var = 10

def function_with_local_scope():
    # Local scope variable
    local_var = 5
    print("Inside the function:", local_var, global_var)

# Calling the function
function_with_local_scope()

# Trying to access local_var outside the function (will result in an error)
# print("Outside the function:", local_var)

def outer_function():
    outer_var = "I'm from the outer function"
    
    def inner_function():
        inner_var = "I'm from the inner function"
        print(inner_var)
        print(outer_var, global_var)  # Accessing variable from the enclosing scope
    
    inner_function()

outer_function()

# Trying to access inner_var outside the inner function (will result in an error)
# print("Outside inner function:", inner_var)

# Global variable can be accessed anywhere
print("Global variable:", global_var)
