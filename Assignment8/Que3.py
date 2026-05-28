

def add():
    sum =0
    num =int(input("enter number:"))
    for i in range(1,num):
        sum = sum + i
    print("sum is",sum)
add()    


def factorial():
    sum = 0 
    fact = 1
    num =int(input("enter number:"))
    for i in range(1, num):
        fact = fact * i
        sum = sum + fact
    print("sum of factorial is",sum)
factorial()    


def power():
    sum = 0
    num = int(input("enter number:"))
    for i in range(1,num):
        sum = sum + (i ** i)
    print("sum is",sum)
power()        
