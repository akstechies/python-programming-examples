a = 7

""" # * If the natural number is greater than 1 and having no positive divisors other than 1 and the number itself etc.
* For example: 3, 7, 11 etc are prime numbers.
* Other natural numbers that are not prime numbers are called composite numbers.
* For example: 4, 6, 9 etc. are composite numbers. """

if a > 1:
    for j in range(2, int(a/2) + 1):
        if a%j == 0:
            print (a, " is not prime")
            break
    else:
        print (a, " is prime")
else:
    print ("a is ", a)

print("=========================================")

# TODO: Prime Number in Range
min_range = 5
max_range = 50
prime_list = []
for i in range(min_range, max_range):
    if(i > 1):
        for j in range(2, int(a/2) + 1):
            if i%j == 0:
                print (i, " is not prime")
                break
        else:
            prime_list.append(i)
            print (i, " is prime")
    else:
        print ("j is ", i)
print(prime_list)