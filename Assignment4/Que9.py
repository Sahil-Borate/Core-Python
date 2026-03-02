

####WAP to print all numbers in a range divisible by a given number.

num = int(input("enter number:"))
divisor = int(input("enter divisor:"))
for i in range(1,num):
    if(i % divisor == 0):
        print(i)

else:
    print("there is no any number which is divisible by given number.")