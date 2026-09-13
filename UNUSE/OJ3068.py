"""LEAP YEARS"""
year = int(input())
if year <= 1582:
    if not year%4:
        print("yes")
    else:
        print("no")
elif not year%400:
    print("yes")
elif not year%4 and year%100 :
    print("yes")
else:
    print("no")
