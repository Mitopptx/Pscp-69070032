"""triangle"""
def main():
    """triangleeee"""
    a=int(input())
    b=int(input())
    c=int(input())
    temp = 0
    if (a>c and a>b) and (b**2)+(c**2)==a**2:
        temp = 1
    elif b>c and b>a and (a**2)+(c**2)==b**2:
        temp = 1
    elif c>b and c>a and (a**2)+(b**2)==c**2:
        temp = 1
    if a+b>c and a+c>b and c+b>a:
        if a==b and b==c:
            print("EQUILATERAL")
        elif temp == 1:
            print("RIGHT TRIANGLE")
        elif (a==b and a!=c) or (a==c and a!=b):
            print("ISOSCELES")
        elif(b==c and b!=a):
            print("ISOSCELES")
        else:
            print("SCALENE")
    else:
        print("NOT A TRIANGLE")
main()
