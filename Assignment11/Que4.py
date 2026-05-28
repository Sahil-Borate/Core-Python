
li = [45,23,56,87,96,54]
num = len(li)
for i in range(num):
    for j in range(0,num-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]

sec_largest = li[-2]
print("Second Largest Element is :",sec_largest)
