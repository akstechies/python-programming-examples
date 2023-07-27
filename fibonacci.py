n = 10
fib = 1
count = 0

a = 0
b = 1
for i in range(n):
    print(a)            # a:0;    a:1;       a:2  
    c = a+b             #c=0+1=1; c= 1+1=2;  c=1+2=3  
    a = b               #a=1    ; a=1;       a=2  
    b = c               #b=1    ; b=2;       b=3  

