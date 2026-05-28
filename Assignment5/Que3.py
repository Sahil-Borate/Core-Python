
# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


num =int(input("enter number of passenger:"))
ticket = int(input("enter the ticket price: "))

total_amount = 0

for i in range(1,num):
    age = int(input(f"enter the age of passengers {i}: "))
    if(age < 12):
        discount = ticket * 0.30
    elif(age > 59):
        discount = ticket * 0.50
    else:
        discount = ticket
    total_amount = total_amount + discount
print(f"total amount for all people is",total_amount)            

                   
                   

