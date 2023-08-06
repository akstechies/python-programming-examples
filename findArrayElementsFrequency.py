arr = [1, 2, 8, 3, 2, 2, 2, 5, 1 ]
countDict = {}

for x in arr:
    if x in countDict:
        countDict[x] += 1
    else:
        countDict[x] = 1

print(countDict)