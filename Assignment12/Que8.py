
str = "what_is_your_name"

new_str = " "

for i in range(len(str)):
    if i % 2 == 0:
        new_str += str[i]

print("original String is:",str)

print('New String is:',new_str)

