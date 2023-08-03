a = 12
b = 8

smaller = a
if a > b:
    smaller = b

hcf = 0
for i in range(1, smaller):
    if a % i == 0 and b % i == 0:
        hcf = i

print(hcf)