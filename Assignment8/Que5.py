
def prime():
    sum = 0
    num = int(input("enter number:"))
    for num in range(2,num):
        count =  0
        for i in range(1,num):
            if num % i == 0:
                count = count + 1
        if count == 2:
            sum = sum + num        
    print("sum of prime number is",sum)
prime()            




def sum_prime(n):
    s = 0
    for num in range(2, n+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count = count + 1
        if count == 2:
            s = s + num
    return s

n = int(input("Enter number: "))
print("Sum of prime numbers:", sum_prime(n))

