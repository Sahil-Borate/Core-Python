

####WAP to print sum of series upto n using while loop.

num = int(input("enter number:"))
i = 1
sum = 0
while(i <= num):
      sum = sum + i
      i += 1
      print(sum)




####WAP to print sum of series upto n using for loop

num = int(input("enter number:"))
sum = 0
for i in range(1,num+1):
     sum = sum + i
     print(sum)