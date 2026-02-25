
#take the input from the user
num = int(input("enter the three digit number:"))
rev = 0
#apply the condition
if(num > 0 ):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print("it is a palindrome number.")
else:
    print("it is not palindrome number.")
    


