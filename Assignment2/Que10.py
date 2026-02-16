
#take the input from the user
num = int(input("enter the three digit number"))

#calculate the solution
hundreds = num // 100        
tens = (num // 10) % 10     
units = num % 10

reversed_num = (units * 100) + (tens * 10) + hundreds

#displayed result
print(f"the reversed number is {reversed_num} ")