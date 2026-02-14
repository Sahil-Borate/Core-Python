
#take the input from user
nums = int(input("enter the three digit number"))

#Get the first,second and third digit       
hundreds = nums // 100
tens = (nums // 10) % 10
units = nums % 10

#calculate the digits sum
Digits_Sum = hundreds + tens + units

#display result
print(f"the total sum is {Digits_Sum} ")

