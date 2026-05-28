
###check the number is armstrong or not.

num = int(input("enter number:"))
sum = 0
temp = num
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** digits)
    temp = temp // 10
if sum == num :
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")

### to check number is armstrong or not using recursive function

def armstrong(n,digits):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** digits) + armstrong(n // 10, digits)

num = int(input("enter number:"))
digits = len(str(num))
result = armstrong(num , digits)

if result == num:
    print(f"{result} is armstrong number")
else:
    print(f"{result} is not armstrong  number")