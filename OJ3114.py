"""Plane"""
import math
In = float(input())
Out = float(input())
if Out<0 or Out> 24:
    Out= -1
elif Out<In:
    Out+=24
hour = math.ceil(Out-In)
if (In*100)%100>60 or (Out*100)%100>60 or In>24:
    print("ERROR")
elif In<0 or Out<0:
    print("ERROR")
elif Out-In <= 0.16:
    print("FREE")
else:
    if hour == 1:
        print("25")
    elif hour ==2:
        print("50")
    elif hour ==3:
        print("80")
    elif hour ==4:
        print("110")
    elif hour == 5:
        print("145")
    elif hour == 6:
        print("180")
    else:
        print("250")
