arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
evenList = []

for i in range(len(arr)):
    if (i+1) % 2 == 0:
        evenList.append(arr[i])

print(evenList)

# LIST COMPREHENSION

newEvenList = [ arr[x] for x in range(len(arr)) if (x+1) % 2 == 0 ]
print(newEvenList)