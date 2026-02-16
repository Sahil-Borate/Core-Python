
#take the input from the user
amount = int(input("enter the amount "))  

#calculate the solutions
notes2000 = amount // 2000
amount = amount% 2000

notes500 = amount / 500
amount = amount % 500

notes100 = amount // 100
amount = amount % 100

notes50 = amount // 50
amount = amount % 50

notes10 = amount // 10
amount = amount % 10

notes1 = amount

#display the results
print("2000 x",notes2000)
print("500 x",notes500)
print("100 x",notes100)
print("50 x",notes50)
print("10 x",notes10)
print("1 x",notes1)