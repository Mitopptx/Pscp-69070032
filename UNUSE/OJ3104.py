"""TIC TOKET"""
age,day = input().split()
age = int(age)
if age <5:
    price=0
elif age >=19:
    price =150
else:
    price = 100
if day == "Wed":
    price //= 2
print(price)
