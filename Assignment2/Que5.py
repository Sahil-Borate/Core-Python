
#take the input from user
cost_price = int(input("enter the cost price of book "))
discount = int(input("enter the discount of book "))

#calculate the discount and selling price
discount = cost_price * (discount / 100)
selling_price = cost_price - discount

#display result

#print(f"the discount of book is {discount} and The Selling Price Of Book Is {selling_price}")
print(f"The Selling Price Of Book is {selling_price} ")