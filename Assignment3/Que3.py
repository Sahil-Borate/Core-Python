
#take the input from the user
angle1 = int(input("enter angle one:"))
angle2 = int(input("enter angle two:"))
angle3 = int(input("enter angle three:"))

sum = angle1 + angle2 + angle3

#apply the condition
if(sum == 180 ):
   print(f"{sum} is a valid angle of triangle:")
else:
   print(f"{sum} is not a valid angle of triangle")