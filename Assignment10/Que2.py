
li = [62,77,80,90,50]

max = li[0]
for ind in range(1,len(li)):
    if li[ind] > max :
        max = li[ind]
    else:
        min = li[ind]
        print("the Min Element From List is :",min)

print("The Max Element From List is :",max)
