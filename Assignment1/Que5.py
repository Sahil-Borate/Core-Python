
#declare the four variables
p = float(input("enter the principal amount"))
r = float(input("enter the rate of interest")) 
t = float(input("enter the time"))
n = float(input("enter the compounding frequencey"))

#calculate the compound interest
CompoundInterest = p + (1 + r / n) *n*t

#declare a variable
a = CompoundInterest

#calculate the total interest
totalInterest = a - p

#display the result
print("the compound interest is",CompoundInterest)
print("the total interest is",totalInterest)

