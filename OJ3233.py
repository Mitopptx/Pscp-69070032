"""no lottery for rabbit"""
ch,num = map(str,input().split())
chw,numw = map(str,input().split())
if ch == chw:
    if num == numw:
        print ("1000000")
    elif num[2:4]== numw[2:4]:
        print("2000")
    elif num[3:4]== numw[3:4]:
        print("1000")
    else:
        print("0")
else:
    if num == numw:
        print("100000")
    elif num[2:4] ==numw[2:4]:
        print("200")
    elif num[3:4] == numw[3:4]:
        print("100")
    else:
        print("0")
