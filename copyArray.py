arr = [1,2,3,4,5]

arr2 = arr.copy()
print(arr2)

# ==========

arr3 = [ x for x in arr ]
print(arr3)

# ==========

arr4 = []
for y in arr:
    arr4.append(y)
print(arr4)

# ==========

arr5 = [None] * len(arr)

for i in range(len(arr)):
    arr5[i] = arr[i]

print(arr5)