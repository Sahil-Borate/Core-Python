
###Write A Program To Print First N Prime Numbers

num = int(input("enter number:"))
for num in range(num):
    if(num > 1):
        for i in range(2,num):
            if (num % i == 0):
                break
        else:
            print(num)    