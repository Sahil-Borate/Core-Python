
li = [45,65,98,23,45,65,23,87]
li = list(set(li))
print(li)


li = [45,65,98,23,45,65,23,87]
unique = []
for i in li:
    if i not in unique:
        unique.append(i)
print(unique)