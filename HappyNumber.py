num = 32
result = 0

def getCount(tempX):
    i = 0
    while tempX > 0:
        tempX //=10
        i+=1
    return i

while num > 0:
    temp = num % 10
    result +=  temp ** 2
    num //=10 
    if(getCount(result) > 1 and num == 0):
        num = result
        result = 0

print(result)


# ====================
result = 0
num = 32

while True:
    while num > 0:
        temp = num % 10
        result +=  temp ** 2
        num //=10 
        
    if result < 10:
        break

    num = result
    result = 0

print(result)
