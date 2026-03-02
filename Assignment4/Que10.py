
##WAP to check if given number is Perfect Number.

num = int(input("enter number:"))
sum = 0
for i in range(1,num):
    if(num % i == 0):
        sum = sum + i
        if(sum == num):
            print(f"{sum} is a perfect number.")
        else:
            print(f"{sum} is not perfect number.")