
##to check number is prime or not.

num = int(input("enter number:"))
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not prime number.")
        break
else:
    print(f"{num} is prime number.")

##to check number is prime or not using recursive function.

def prime(num, i=2):
    if num <= 1 :
        return False
    if i == num :
        return True
    if num % i == 0:
        return False
    return prime(num ,i+1)
num = int(input("enter number:"))
if prime(num):
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")