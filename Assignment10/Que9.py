
n= int(input("enter number:"))
li = []
for i in range(n):
    num = int(input("enter number :"))
    num = i + 1
    li.append(num)
# print(li)

even_li = []
odd_li =[]
for num in range(len(li)):
    if num  % 2 == 0:
        even_li.append(num)
    else:
        odd_li.append(num)

print("Original List is:",li)
print("even_li is:",even_li)
print("odd_li is:",odd_li)

