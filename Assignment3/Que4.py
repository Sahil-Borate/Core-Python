
#take the input from the user
x = int(input("enter first side:"))
y = int(input("enter second side:"))
z = int(input("enter third side:"))

#apply the condition
if(x + y > z and x + z > y and y + z > x):
    print(f"it is a valid triangle")
else:
    print(f"it is not valid triangle")



