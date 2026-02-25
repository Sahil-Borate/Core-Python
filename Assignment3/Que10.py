
#take the input from the user
Gender = input("enter the Gender:")
Age = int(input("enter the age:"))

#apply the condition
if(Gender.lower() in ['f','female']):
    if(Age >= 18):
        print("Eligible For Marriage.")
    else:
        print("Not Eligible For Marriage.")
else:
    if(Age >= 21):
        print("Eligible for Marriage.")
    else:
        print("Not Eligible For MArriage.")




