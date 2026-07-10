"""quadrant"""
x = float(input())
y = float(input())
if not x and not y:
    print("O")
elif not x:
    print("Y")
elif not y:
    print("X")
elif x>0:
    if y>0:
        print("Q1")
    elif y<0:
        print("Q4")
elif x<0 :
    if y>0:
        print("Q2")
    elif y<0:
        print("Q3")
