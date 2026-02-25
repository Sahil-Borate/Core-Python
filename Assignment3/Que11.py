
#declare and initialize the variable 
total_amount = 0

#use the for loop
for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))
    ticket = float(input(f"Enter ticket amount for person {i}: "))

#use the branching
    if age < 12:
        discount = ticket * 0.30
        final_price = ticket - discount
    elif age > 59:
        discount = ticket * 0.50
        final_price = ticket - discount
    else:
        final_price = ticket

    total_amount += final_price

#display the result
print("Total ticket amount for all 5 people =", total_amount)



####Another Way To Execute The Program



#take the input from the user
Age1 = int(input("enter first people Age:"))
Age2 = int(input("enter Second people Age:"))
Age3 =int(input("enter Third people Age:"))
Age4 =int(input("enter fouth people Age:"))
Age5 = int(input("enter fifth people Age:"))

people1 = int(input("enter the first people ticket amount:"))
people2 = int(input("enter the Second people ticket amount:"))
people3 = int(input("enter the Third people ticket amount:"))
people4 = int(input("enter the fourth people ticket amount:"))
people5 = int(input("enter the fifth people ticket amount:"))

#add the people ticket amount
Total_Amount = people1 + people2 + people3 + people4 + people5

#apply the conditio
if(Age1,Age2,Age3,Age4,Age5 < 12):
   discount = Total_Amount * 0.30
   final_price = Total_Amount - discount
elif(Age1,Age2,Age3,Age4,Age5 > 59):
    discount = Total_Amount * 0.50
    final_price = Total_Amount - discount
else:
    final_price = Total_Amount
    Total_Amount += final_price
print(f"{final_price} is the total ticket amount for all 5 people.")
