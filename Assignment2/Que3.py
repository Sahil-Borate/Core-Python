
#it is the fixed measurement
CM_PER_FOOT = 30.48
CM_PER_INCH = 2.54

#take the input from the user
feets = float(input("enter feet"))
inches = float(input("enter inches"))

#calculate the total centimeters
total_cm = (feets * CM_PER_FOOT) + (inches * CM_PER_INCH)

#breakdown into meters and centimeters
meters = int(total_cm // 100)
centimeter = total_cm % 100

#display result
print(f"Result: {meters} meter and {centimeter} centimeter ")


