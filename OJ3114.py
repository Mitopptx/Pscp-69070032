import math
In = float(input())
Out = float(input())
if Out<In:
    Out+=24
hour = math.ceil(Out-In)
if (In*100)%100>60 or (Out*100)%100>60:
    print("ERROR")
elif Out-In <= 0.16:
    print("FREE")
else:
    if hour == 1:
        print("25บาท")
    elif hour ==2:
        print("50บาท")
    elif hour ==3:
        print("80บาท")
    elif hour ==4:
        print("110บาท")
    elif hour == 5:
        print("145บาท")
    elif hour == 6:
        print("180บาท")
    else:
        print("250บาท")
