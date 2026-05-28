
def odd():
    sum = 0
    num = int(input("enter number:"))
    for i in range(1,num):
        if i % 2 !=0:
           sum = sum + i
    print("sum of odd Number is",sum)
odd()
       
