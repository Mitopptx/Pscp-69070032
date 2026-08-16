"""w"""
a = int(input())
b = int(input())
goal = int(input())
buse = goal//5
if buse <=b:
    goal -= buse*5
else:
    goal -= b*5
if goal<=a:
    print(goal)
else:
    print("-1")
