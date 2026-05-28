
## Write a program to prompt user to enter userid and password. If Id and
## password is incorrect give him chance to re-enter the credentials. Let him try 3
## times. After that program to terminate.


correct_user_name = "Sahilb"
correct_password = "3012"

max_attempt = 3

for attempt in range(1,max_attempt+1):
    user_name = input("Enter Username:")
    password = input("enter password:")


    if(user_name == correct_user_name and password == correct_password):
        print("username and password entered successfully.")
        break
    else:
        print("incorrect username and password.")


    
