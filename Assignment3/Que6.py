
#take the input from the user
cost_price = float(input("enter the cost price:"))
selling_price = float(input("enter the selling price:"))

#apply the Conditiom
if(selling_price > cost_price):
    profit = selling_price - cost_price
    print(f"{profit} profit")
elif(cost_price > selling_price):
    loss = cost_price - selling_price
    print(f"{loss} loss")
else:
    print("No Profit,No loss")
