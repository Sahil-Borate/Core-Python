
str = "I was paid 15000 rupees bill of dinner at Yesterday Night."

letters= 0

digits = 0

for ch in str:
    if ch >= '0' and ch <= '9':
        digits += 1

    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1

print(digits)

print(letters)