#  156 = 1 + 5 + 6 = 12 , 156 % 12 = 0

num = 156
result = 0
while num > 0:
    temp = num % 10
    result += temp
    num //= 10

if  num % result == 0:
    print("Harshadwa")
else:
    print("Nibba")

print(result)