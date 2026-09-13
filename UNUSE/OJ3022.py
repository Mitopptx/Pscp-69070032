"""degree"""
degree = float(input())
char1 = input()
char2 = input()
if char1 != 'C':
    if char1 == 'F':
        degree=(degree-32)*5/9
    elif char1 == 'K':
        degree = degree - 273.15
    elif char1 == 'R':
        degree=(degree*5/9)-273.15
if char2 == 'C':
    print(f"{degree:.2f}")
elif char2 == 'F':
    print(f"{degree*9/5+32:.2f}")
elif char2 == 'K':
    print(f"{degree + 273.15:.2f}")
elif char2 == 'R':
    print(f"{(degree+273.15) *9/5:.2f}")
