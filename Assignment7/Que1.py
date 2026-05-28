

# upper part
for i in range(1, 6):
    for j in range(1, 6*2):
        if j == 6-i+1 or j == 6+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# lower part
for i in range(6-1, 0, -1):
    for j in range(1, 6*2):
        if j == 6-i+1 or j == 6+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

