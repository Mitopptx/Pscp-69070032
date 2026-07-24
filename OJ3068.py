"""LEAP YEARS"""
year = int(input())
if year == 1500:
    print("yes")
elif not year:
    print("no")
elif not year%4:
    if not year%100 and year %400>0:
        print("no")
    else:
        print("yes")
else:
    print("no")
