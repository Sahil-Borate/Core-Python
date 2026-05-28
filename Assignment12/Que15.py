
str1 = "Python is easy language"

str2 = "Python is powerful language"

count1 = 0

count2 = 0

for ch in str1:
    count1 += 1

for ch in str2:
    count2 += 1

if count1 > count2:
    print("str1 is Larger String.")
else:
    print('str2 is larger String.')