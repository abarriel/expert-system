year = input('Write a year: ')
print(year)
year = int(year)
bisex = False

if year % 400 == 0:
    bisex = True
elif year % 100 == 0:
    bisex = False
elif year % 4 == 0:
    bisex = True
else:
    bisex = False

if bisex:
    print("Year is bisex")
else:
    print("Year is not a bisex")