"""season"""
month = int(input())
date = int(input())
if date >= 21:
    month = month+1
# if month == 1 and month == 2 and month == 3:
if 1 <= month <= 3:
    print("winter")
elif 4 <= month <= 6:
    print("spring")
elif 7 <= month <= 9:
    print("summer")
elif 10 <= month <= 12:
    print("fall")
else:
    print("winter")
