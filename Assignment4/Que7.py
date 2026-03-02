

###WAP to print all integers upto n that aren’t divisible by 2 and 3.

num = int(input("enter number:"))

for i in range(1,num):
    if(i % 2 != 0 and i % 3 != 0 ):
        print(i)





