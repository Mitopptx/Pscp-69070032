"""BunBUn"""
size,style = input().split()
stri = input()
top = "a"
mult = 0
price = 0
if stri != "N":
    top,num = stri.split()
    num = int(num)
if size== "S":
    mult =0
elif size == "M":
    mult = 20
elif size =="L":
    mult= 40
if style =="R":
    price = 60+mult
elif style == "T":
    price = 80+mult
if top =="P":
    price += 15*num
elif top == "E":
    price += 10*num
print(price)
