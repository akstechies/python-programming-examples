import string

punc = string.punctuation

text = "Hello, world! jdfhj,,,,,  jsdh!!"

newText = ""

for x in text:
    if x not in punc:
        newText += x

print(newText)