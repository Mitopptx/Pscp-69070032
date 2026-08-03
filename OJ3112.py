"""BooBa"""
boba,g1 = input().split()
tea,sweet,g2 = input().split()
g1 = float(g1)
g2 = float(g2)
s=0
num=0
if sweet=="1":
    s = 10
elif sweet == "2":
    s = 15
elif sweet =="3":
    s=20
if boba =="H":
    num = g1*5
elif boba == "J":
    num = g1*2
elif boba =="O":
    num = g1*3
if tea == "R":
    s += s//4
elif tea == "T":
    if sweet =="2":
        s =20
    else:
        s *= 1.5
calories = num+(s*g2)
if calories *10 %10 >0:
    print(calories)
else:
    print(int(calories))
