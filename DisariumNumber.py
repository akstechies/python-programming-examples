x = 175
result = 0

tempX = x
i = 0
#get length of number
while tempX > 0:
    tempX //=10
    i+=1

while x > 0:
    temp = x % 10
    result = result + temp ** i
    x //= 10
    i-=1

print(result)