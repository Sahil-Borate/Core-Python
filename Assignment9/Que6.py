
##print the fibonacci series.

a = -1
b = 1
num = int(input("enter number:"))
for i in range(1,num):
    c = a + b
    print(c,end=" ")
    a = b
    b = c

## print fibonacci series using recursive function

def fibonacci(n, a=-1, b=1):
    if n == 0 :
        return
    c = a + b
    print(c,end=" ")
    fibonacci(n-1,b,c)
num = int(input("enter number:"))
fibonacci(num)


