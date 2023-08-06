arr = [1, 2, 3, 4, 5]

arrLen = len(arr)

revArr = []

i = arrLen
while i > 0:
    i -= 1
    print(i)
    revArr.append(arr[i])

print(revArr)

