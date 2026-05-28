
##WAP to calculate the M to the Power N.

m = int(input("enter base number:"))
n = int(input("enter power number:"))
result = 1
for i in range(n):
    result = result * m
print(result)


##WAP to calculate the M to the Power N using recursive function.

def power(m,n):
    if n == 0:
        return 1
    return m * power(m,n-1)
m = int(input("enter base number:"))
n = int(input("enter power number:"))
res = power(m,n)
print(res)
