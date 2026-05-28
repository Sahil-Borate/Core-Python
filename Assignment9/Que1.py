
##print the sum of factorial.

num = int(input("enter number:"))
fact = 1 
sum = 0
for i in range(1,num + 1):
    fact = fact * i
    sum = sum + fact
print(sum)    

###print the sum of factorial using recursive function.

def fact(n):
    if  n == 1:
        return 1
    else:
        return n * fact(n - 1)

def sum_series(n):
    if n == 1:
        return 1
    return fact(n) + sum_series(n - 1)

num = int(input("enter number:"))
result = sum_series(num)
print("sum of series is",result)
