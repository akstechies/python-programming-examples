#======================================
# TODO: DECORATORS
# * Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself. They are represented the @decorator_name in Python and are called in a bottom-up fashion. For example:

# ? Simple Decorators
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

@lowercase_decorator
def hello():
    return "Hello WORLD"
print(hello())

print("============================================")

# TODO: Decorators with Arguments
# * The beauty of the decorators lies in the fact that besides adding functionality to the output of the method, they can even accept arguments for functions and can further modify those arguments before passing it to the function itself. The inner nested function, i.e. 'wrapper' function, plays a significant role here. It is implemented to enforce encapsulation and thus, keep itself hidden from the global scope.

def capitalize(function):
    def capitals(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return capitals

@capitalize
def say_hello(name1, name2):
   return 'Hello ' + name1 + '! Hello ' + name2 + '!'
print(say_hello('sara', 'ansh'))

print("============================================")

# TODO: Other Examples - with two decorator functions

# decorator function to convert to lowercase
def lowercase_decorator(function):
   def wrapper():
       func = function()
       string_lowercase = func.lower()
       return string_lowercase
   return wrapper

# decorator function to convert to uppercase
def uppercase_decorator(function):
   def wrapper():
       func = function()
       string_uppercase = func.upper()
       return string_uppercase
   return wrapper

# decorator function to split words
def splitter_decorator(function):
   def wrapper():
       func = function()
       string_split = func.split()
       return string_split
   return wrapper


@splitter_decorator # this is executed next
@uppercase_decorator
@lowercase_decorator # this is executed first
def hello():
   return 'Hello World'
print(hello())   # output => [ 'hello' , 'world' ]
