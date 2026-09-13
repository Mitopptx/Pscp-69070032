"""festiwalk"""
walk = input()
x=0
y=0
for i in walk:
    if i == "N":
        y +=1
    elif i == "S":
        y -=1
    if i == "E":
        x +=1
    elif i == "W":
        x -=1
print(x,y,abs(x)+abs(y))
