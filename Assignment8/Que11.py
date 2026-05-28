
def count_digits(n):
    count = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        count += 1
    return count

def armstrong_sum(n, digits):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp = temp // 10
    return sum

def check_armstrong(n):
    digits = count_digits(n)
    result = armstrong_sum(n, digits)

    if result == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


num = int(input("Enter a number: "))
check_armstrong(num)