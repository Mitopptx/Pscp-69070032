"""BooBa"""
boba,g1 = input().split()
tea,sweet,g2 = input().split()
g1 = int(''.join(c for c in g1 if c.isdigit()))
g2 = int(''.join(c for c in g2 if c.isdigit()))
s=0
ca=0
if sweet=="1":
    s = 10
elif sweet == "2":
    s = 15
elif sweet =="3":
    s=20
if boba =="H":
    ca = g1*5
elif boba == "J":
    ca = g1*2
elif boba =="O":
    ca = g1*3
if tea == "R":
    s += s//4
elif tea == "T":
    if sweet =="2":
        s =20
    else:
        s *= 1.5
print(int(ca+(s*g2)))
