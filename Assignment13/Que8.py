
str = input("enter a string :")

words = str.split()

dict = {}

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(dict)