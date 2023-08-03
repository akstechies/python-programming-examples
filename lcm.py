x = 40
y = 60

greater = x
if(y > x):
    greater = x

while(True):
    if(greater % x == 0 and greater % y == 0):
        lcm = greater
        break
    greater += 1

print(lcm)