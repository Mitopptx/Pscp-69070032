"""miniexam"""
def main():
    """calculate"""
    import math
    r = float(input())
    a = float(input())
    b = float(input())
    circle = 2*math.pi*r
    rectangle = a+a+b+b
    temp = abs(round(circle-rectangle,5))
    if circle>rectangle:
        print("Circle is longer\n",temp,sep='')
    elif rectangle>circle:
        print("Rectangle is longer\n",temp,sep='')
    else:
        print("Equal\n0.00000")
main()
