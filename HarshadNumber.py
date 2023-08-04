#  156 = 1 + 5 + 6 = 12 , 156 % 12 = 0

num = 5764231
tempNum = num
result = 0
while tempNum > 0:
    temp = tempNum % 10
    result += temp
    tempNum //= 10

if  num % result == 0:
    print("Harshadwa")
else:
    print("Nibba")

print(result)