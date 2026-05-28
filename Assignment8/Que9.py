
def palindrome():
    num = int(input("enter number:"))
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if original == rev:
        print("the number is paindrome.")
    else:
        print("the number is not palindrome.")
palindrome()            
