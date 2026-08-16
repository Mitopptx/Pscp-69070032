"""no lottery for rabbit"""
ch,num = map(str,input().split())
chw,numw = map(str,input().split())
if ch == chw:
    if num == numw:
        print ("1000000")
    elif num[2:5]== numw[2:5]:
        print("2000")
    elif num[3:5]== numw[3:5]:
        print("1000")
    else:
        print("20")
else:
    if num == numw:
        print("100000")
    elif num[2:5] ==numw[2:5]:
        print("200")
    elif num[3:5] == numw[3:5]:
        print("100")
    else:
        print("0")
