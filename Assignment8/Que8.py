
def reverse():
    rev = 0
    num = int(input("enter number:"))
    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10
    print(rev)   
reverse()        