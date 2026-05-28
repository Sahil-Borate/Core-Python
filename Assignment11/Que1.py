
num = int(input("Enter number :"))
even_li1 = []
odd_li2 = []
for i in range(num):
    if i % 2 == 0:
        even_li1.append(i)
    elif i % 2 != 0:
        odd_li2.append(i)
print(f"Even NUmber List Is :",even_li1)
print(f"Odd Number List Is :",odd_li2)