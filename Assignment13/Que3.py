
dict = {'ID':101,'name':'sahil','Age':23,'city':'pune'}

key = input("enter key to search:")

if key in dict:
    print('key is available')
else:
    print("key not available")