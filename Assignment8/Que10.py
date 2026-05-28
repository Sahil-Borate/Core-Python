
def leap_year():
    year = int(input("enter number:"))
    if(year % 4 == 0 and year % 100 != 0):
        print(f"{year} is leap year.")
    else:
        print(f"{year} is not leap year")
leap_year()        