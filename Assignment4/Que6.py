
##write a program to check number is prime or not.

num = int(input("enter number:"))
for i in range(2,num):
    if(num % i == 0):
     print(f"{num} is not prime number.")
     break
else:
    print(f"{num} is a prime number.")

