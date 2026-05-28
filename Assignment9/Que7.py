
##print sum of digit

num = int(input("enter number:"))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)


#print sum of digit using recursive function

def sum_digit(n,sum=0):
    if n == 0:
        return sum
    digit = n % 10
    sum = sum + digit
    return sum_digit(n // 10, sum)
num = int(input("enter number:"))
res = sum_digit(num)
print(f"sum of digit is",res)
    