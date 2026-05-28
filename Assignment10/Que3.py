
li = [56,92,65,78,82,90]

max = li[0]
sec_max = 0
for ind in range(len(li)):
    if li[ind] > max:
        sec_max = max 
        max = li[ind]
    elif li[ind] > sec_max:
        sec_max = li[ind]
        
print("The Max Element From List is :",max)
print("THe Second Max Element From list is :",sec_max)

