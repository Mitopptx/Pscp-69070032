number = int(input())
degree = input()
if degree == 'F':
    number = (number-32)*5/9
if number <=0:
    print("solid")
elif number >= 100:
    print("gas")
else:
    print("liquid")
