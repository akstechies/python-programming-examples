num = int(input("Enter a number: "))
n = str(num)
pow = len(n)
k=0
for i in n:
    j = int(i)
    k += j**pow

if k == int(n):
    print(f"{num} is Armstrong! => {k}")
else:
    print(f"{num} is Not Armstrong! => {k}")

