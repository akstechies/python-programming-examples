#======================================
# TODO: Dict and List comprehensions
# * Python comprehensions, like decorators, are syntactic sugar constructs that help build altered and filtered lists, dictionaries, or sets from a given list, dictionary, or set. Using comprehensions saves a lot of time and code that might be considerably more verbose (containing more lines of code).s

my_list = [1, 2, 3, 4, 5]

squared_list = [x**2 for x in my_list]
cube_list = [x**3 for x in my_list]

print(squared_list)
print(cube_list)

print("======================================")
# * Now doing comprehension with conditions

squared_list_with_condition = [x**2 for x in my_list if (x**2 % 2) != 0]
print(squared_list_with_condition)

print("======================================")
# * Combining multiple lists into one

a = [1, 2, 3]
b = [4, 5, 6]

zip_a_b = zip(a, b)
a_b = list(zip_a_b)
print(a_b)
print(type(a_b))

for (x, y) in a_b:
    print(y)

firstList = [(x+y) for (x, y) in zip(a,b)]
print(firstList)

print("======================================")
# * Creating DICT

dict_list = {x:x**2 for x in my_list}
print(dict_list)

print("======================================")
# * Flattening a multi-dimensional list

my_list = [[10,20,30],[40,50,60],[70,80,90]]
flattened = [x for temp in my_list for x in temp]
print(flattened)