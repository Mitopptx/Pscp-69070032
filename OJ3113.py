size,style = input().split()
str = input()
top = "a"
if str != "N":
    top,num = str.split()
    num = int(num)
if size== "S":
    multiply =0
elif size == "M":
    multiply = 20
elif size =="L":
    multiply = 40
if style =="R":
    price = 60+multiply
elif style == "T":
    price = 80+multiply
if top =="P":
    price += 15*num
elif top == "E":
    price += 10*num
print(price)
