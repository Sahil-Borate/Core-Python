
##write a program to print reverse number.

num = int(input("enter number:"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(rev)

##write a program to print reverse number using recursive function.

def reverse(n,rev= 0):
    if n == 0 :
        return rev
    digit = n % 10
    rev = (rev * 10) + digit
    return reverse(n // 10,rev)
num = int(input("enter number:"))
res = reverse(num)
print(res)
