
####WAP to print factorial of a number using for loop.
num = int(input("enter number"))
fact = 1
for i in range(num):
     fact = fact * num
     num -= 1
     print(fact)



####WAP to print factorial of a number using for loop.
num = int(input("enter number"))
fact = 1
while(num > 0):
    fact = fact * num
    num -= 1
    print(fact)
