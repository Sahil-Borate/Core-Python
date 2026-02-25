
#take the input from the user
Marathi = int(input("enter marks of marathi:"))
Hindi = int(input("enter marks of hindi:"))
English = int(input("enter marks of english:"))
Maths = int(input("enter marks of maths:"))
Geography = int(input("enter marks of geography:"))

sum = (Marathi + Hindi + English + Maths + Geography) / 5  

#apply the condition
if(sum >= 91 and sum <= 100):
    print("Grade A.")
elif(sum >= 76 and sum <= 90):
    print("Grade B.")
elif(sum >= 61 and sum <= 75 ):
    print("Grade C.")
elif(sum >= 41 and sum <= 60):
    print("Grade D")
else:
    print("Fail.")
