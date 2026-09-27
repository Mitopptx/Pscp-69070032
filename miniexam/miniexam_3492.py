"""miniexam"""
import math
def main():
    """calculate"""
    r = float(input())
    a = float(input())
    b = float(input())
    circle = 2*math.pi*r
    rectangle = a+a+b+b
    temp = abs(circle-rectangle)
    if circle>rectangle:
        print(f"Circle is longer\n{temp:.5f}")
    elif rectangle>circle:
        print(f"Rectangle is longer\n{temp:.5f}")
    else:
        print(f"Equal\n{temp:.5f}")
main()
