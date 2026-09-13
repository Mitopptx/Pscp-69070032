"""ONE DUEN PI"""
def leap(y):
    """cal leap"""
    return (not y % 400) or (not y % 4 and y % 100)
def calday(y, m, d):
    """sum day"""
    days = 0
    for i in range(1, y):
        if leap(i):
            days += 366
        else:
            days += 365
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(m-1):
        days += month[i]
    if leap(y) and m > 2:
        days += 1
    days += d
    return days
y1= int(input())
m1= int(input())
d1= int(input())
y2= int(input())
m2= int(input())
d2= int(input())
day1 = calday(y1, m1, d1)
day2 = calday(y2, m2, d2)
if abs(day1 - day2) <= 7:
    print(0)
elif day1 < day2:
    print(1)
else:
    print(2)
