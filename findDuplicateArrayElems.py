arr = [1, 2, 8, 3, 2, 2, 2, 5, 1 ]
duplicateArr =  []
duplicateList = []

for x in arr:
    if x in duplicateArr:
        duplicateList.append(x)
    else:
        duplicateArr.append(x)

print(duplicateArr)