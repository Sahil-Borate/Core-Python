

def fibonacci():
    a = -1
    b = 1
    num = int(input("enter number:"))
    for i in range(1,num):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
fibonacci()        