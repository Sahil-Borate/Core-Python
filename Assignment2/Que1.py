
#take the input from the user
hrs = int(input("enter the hours"))
min = int(input("enter the minute"))
sec = int(input("enter the second"))

#calculate the solutions
total_second = (hrs*3600) + (min*60) + 60

#display result
print("total second is",total_second)