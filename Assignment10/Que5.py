
num = int(input("enter a number:"))
li = [56,85,64,98,62,59,98]

if num in li:
    print("The Element Are Present In The List.")
else:
    print("The Element Are Not Present In The List.")
    
ele =li.count(num)
print(ele)