
#declare the three variable and assign the value
a = 1
b = 5
c = 6

#calculate discriminant
d = b**2 - 4*a*c

#calculate the solutions
root1 = (-b + d ** 0.5) / (2 * a)
root2 = (-b - d ** 0.5) / (2 * a)

#display the result
print("the roots are", root1, "and", root2)