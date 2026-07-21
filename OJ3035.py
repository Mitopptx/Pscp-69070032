"""AAR TIKTOK"""
r,x,y=map(float,input().split())
cx = abs((r**2)-(y**2))**0.5
cy = abs((r**2)-(x**2))**0.5
if x<0:
    x *= -1
if y<0:
    y *= -1
if cx==x and cy==y:
    print("ON")
elif cx>x and cy>y:
    print ("IN")
else:
    print ("OUT")
