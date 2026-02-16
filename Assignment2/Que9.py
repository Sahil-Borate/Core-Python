
#take the input from the user
a = int(input("enter the value of a "))
b = int(input("enter the value of b "))

#swap the values
a , b = b , a

#display result
print("the value of a is",a)
print("the value of b is",b)             


#Another way to execute the program


#take the input from the user
a = int(input("enter the value of a "))
b = int(input("enter the value of b "))

#swap the value of a and b
a = a + b
b = a - b
a = a - b

#display result 
print(f"the value of a is {a} and the value of b is {b} ")

