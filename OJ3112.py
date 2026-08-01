boba,g1 = input().split()
tea,sweet,g2 = input().split()
g1=int(g1)
g2=int(g2)
if sweet=="1":
    s = 10
elif sweet == "2":
    s = 15
elif sweet =="3":
    s=20

if boba =="H":
    cal = g1*5
elif boba == "J":
    cal = g1*2
elif boba =="O":
    cal = g1*3
  
if tea == "R":
    s += s//4
elif tea == "T":
    if sweet =="2":
        s =20
    else:
      s *= 1.5
print(cal+(s*g2))
