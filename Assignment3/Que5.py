
#take the input from the user
a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:")) 

#apply the condition
if(a + b > c and a + c > b and b + c > a):
    if(a == b and b== c and a == c):
        print(f"the triangle is is equilateral:")
    else:
        print(f"the triangle is not equilateral:")
    if(a == b ):
        print(f"the triangle is isoscales:")
    else:
        print(f"the tringle is not isoscales:")
else:
    print("the triangle is scalane:")


