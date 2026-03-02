

####WAP to print Fibonacci series upto n.

num = int(input("enter number:"))
a = -1
b = 1
for i in range(num):
    c = a + b
    print(c , end=" ")
    a = b
    b = c


####WAP to print Fibonacci series upto n using while loop.

num = int(input("enter number:"))
a = 0
b = 1
count = 1
while(count <= num ):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1 
