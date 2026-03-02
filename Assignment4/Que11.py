

##WAP to check if given number Strong Number.

num = int(input("enter number:"))
temp = num
Sum_fact = 0
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1,digit+1):
        fact *= i

    Sum_fact += fact
    temp = temp // 10
        
if Sum_fact == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not strong number.")
    
