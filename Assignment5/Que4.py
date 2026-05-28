

## WAP to print Armstrong number within a given range.

start = int(input("enter start number:"))
end = int(input("enter ending number:"))

print(f"armstrong numbers in given rnage are:")

for num in range(start,end+1):
    digits = len(str(num))
    temp = num
    sum = 0

    while(temp > 0):
        digit = temp % 10
        sum += digit ** digits
        temp = temp // 10

    if(sum == num):
        print(f"{num} is an armstrong number.")