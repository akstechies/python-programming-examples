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
