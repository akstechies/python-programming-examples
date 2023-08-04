name = "Ayush"

reverseName = name[::-1]
print(reverseName)

#  ================

nameLen = len(name)
index = nameLen - 1
reversedName = ""
while index >= 0: 
    reversedName += name[index]
    index -= 1
print(reversedName)