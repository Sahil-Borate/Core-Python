
###find the factorial number. 

num = int(input("enter number:"))
fact = 1
for i in range(1,num + 1):
     fact = fact * i 
print(fact)

###find the factorial number using recursive function.

def factorial(n):
     if n == 0:
         return 1
     return n * factorial(n - 1)
num = int(input("enter number:"))
res = factorial(num)
print(res)    

