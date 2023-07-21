import random

some_random = random.random()
print(some_random)

# * Random Number within Range
random_int = random.randint(0, 50)
print(random_int)

range_number = range(20, 30)
rand_list = []
for i in range_number:
    n = random.randint(0, 50) 
    # n = random_int # This will give same values because the value is assigned above
    rand_list.append(n)
print(rand_list)

# * The random module also provides the sample() method, which directly generates a list of random numbers. Below is the example of generating random numbers using the sample() method.

random_sample_list = random.sample(range(40, 69), 6)
print(random_sample_list)