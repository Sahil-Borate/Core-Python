
import random
correct_userid = "admin123"
correct_password = "abc@123"

#take the input from the user
user_id = input("enter the username:")
password = input("enter the passowrd:")
if(user_id == correct_userid and password == correct_password):
    print("login Successful.")

    captcha = random.randint(1000,9999)
    print("enter four digit number",captcha)

    user_captcha = int(input("enter the number:"))

    if(user_captcha == captcha):
        print("verification completed successfully.")
    else:
        print("Failed!, Incorrect Number Entered.")
else:
    print("Invalid userid and Password.")



