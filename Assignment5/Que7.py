

####Write a program to solve the following series:

##1.

num = int(input("enter number:"))
sum = 0
fact =1
for i in range(1,num+1):
    fact = fact * i
    sum = sum + fact
    print(f"sum of series is {sum}.")


##2.

num =int(input("enter number:"))
sum = 0
for i in range(1,num):
    sum = sum + (num ** i)
    print(f"sum of series is {sum}.")


##3.

num = int(input("enter numbers:"))
sum = 0
term = 1
for i in range(num):
      sum = sum + term
      term = term * 2
print(f"sum of series is {sum}")


##4.

a = int(input("enter number:"))
sum = 0
for i in range(1,11):
     term = (a ** i) / i
     sum = sum + term
     print(f"sum of series is {sum}")


##5.

x= int(input("enter number:"))
num = int(input("enter number:"))
sum = 0
sign = 1
denominator = 1
for i in range(1,num+1):
    sum = sum + sign * (x ** i) / denominator
    sign = -sign
    denominator = denominator + 2 
    print(f"sum of series is {sum}")
