
##find the sum of series.

num = int(input("enter number:"))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)

###find sum of series using recursive function.

def sum_series(n,sum = 0):
    if n == 0:
        return sum
    digit = n % 10
    sum = sum + digit
    return sum_series(n // 10,sum)
num = int(input("enter number:"))
res = sum_series(num)
print(f"{res} is a sum of number")