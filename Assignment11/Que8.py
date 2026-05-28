
num = 1

for row in range(10):
    temp = []

    for col in range(10):
        temp.append(num)
        num += 1

    if row % 2 == 1:
        temp.reverse()

    for i in temp:
        print(f"{i:3}",end=" ")

    print()