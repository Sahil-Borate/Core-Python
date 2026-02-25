
correct_userid = "admin123"
correct_password = "abc@123"

#take the input from the user
user_id = input("enter the username:")
password = input("enter the passowrd:")

#apply the condition
if(user_id == correct_userid and password == correct_password ):
    print("login Successful.")
else:
    print("login failed.")

