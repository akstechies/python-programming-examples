elem = [1, 3, 4, 5, 7, 9, 11, 23]

maxElem = max(elem)
newElem = []
for i in range(1, maxElem + 1):
    if i not in elem:
        newElem.append(i)

print(newElem)


# ==============

# Using SET

min_elem = min(elem)
max_elem = max(elem)
all_elements = set(range(min_elem, max_elem + 1))
missing_elements = list(all_elements - set(elem))
print(missing_elements)
