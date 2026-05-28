
str1 = "I am a Clever Boy"

str2 = "How Are You ??"

count1 = 0

count2 = 0

for ch in str1:
    count1 += 1

for ch in str2:
    count2 += 1

if count1 > count2:
    print("Str1 Is A Larger String.")
else:
    print('Str2 is A Larger String.')