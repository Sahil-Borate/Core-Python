
#just declare variable
Total_unit = 0

#take the input from the user
elec_unit = int(input("enter electricity unit charges:"))

#apply the condition
if(elec_unit >= 0 and elec_unit <= 50):
    Total_unit = elec_unit * 0.50
    Total_unit = (Total_unit * 0.20)  + Total_unit 
    print(f"{Total_unit} is a total electricity bill.")

elif(elec_unit >= 51 and elec_unit <= 150):
    Total_unit = elec_unit * 0.75
    Total_unit = (Total_unit * 0.20) + Total_unit
    print(f"{Total_unit} is a total electricity bill.")

elif(elec_unit >= 151 and elec_unit <= 250):
    Total_unit = elec_unit * 1.20
    Total_unit = (Total_unit * 0.20) + Total_unit
    print(f"{Total_unit} is a total electricity bill.")

elif(elec_unit > 251):
    Total_unit = elec_unit * 1.50 
    Total_unit = (Total_unit * 0.20) + Total_unit
    print(f"{Total_unit} is a total electricity bill.")
else:
    print("Invalid Electricity Bill.")


