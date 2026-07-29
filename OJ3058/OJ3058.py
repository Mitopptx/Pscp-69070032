"""BRICK BURG"""
a = int(input())
b = int(input())
goal = int(input())
biggoal = goal//5
if biggoal<=b:
    goal -= (biggoal*5)
    if goal<=a:
        print(goal)
    else:
        print("-1")
else:
    goal -= (b*5)
    if goal<=a:
        print(goal)
    else:
        print("-1")
