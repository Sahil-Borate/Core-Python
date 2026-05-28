
def sum_of_digit():
    num = int(input("enter number:"))
    hundreds = num // 100
    tens = (num // 10) % 10
    unit = num % 10
    Digit_sum = hundreds + tens + unit
    print("sum of three digit is",Digit_sum)
sum_of_digit()    
