
n= int(input("enter Total Number In List:"))
li1 = []
for i in range(n):
    num = int(input("Enter Number :"))
    num = i + 1
    li1.append(num)
print(f"list One is :",li1)

n= int(input("Enter Total Number In List:"))
li2 = []
for i in range(1,n):
    num = int(input("Enter Number:"))
    num = i * 2
    li2.append(num)
print(f"Square List is :",li2)

n = int(input("enter Total Number In The List :"))
li3 = []
for i in range(1,n):
    num = int(input("Enter Number :"))
    num = i ** 3
    li3.append(num)
print(f"Cube List is :",li3)