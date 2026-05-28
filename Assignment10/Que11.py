
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m = int(input("enter number:"))
n = int(input("enter number:"))
for i in range(len(li)):
    if li[i] % m == 0:
        pass
    elif li[i] % n == 0:
        print(n)