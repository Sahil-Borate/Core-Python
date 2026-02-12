#declare the two variable and take the input from user
Angle_A = int(input("enter the value of angle A "))
Angle_B = int(input("enter the value of angle B "))

#calculate the third angle
Angle_c = 180 - (Angle_A + Angle_B) 

#display the result
print("the third angle of triangLe is",Angle_c)