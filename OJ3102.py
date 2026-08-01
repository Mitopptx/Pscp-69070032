year = int(input())
engine = int(input())
if year <=1990:
    if engine <=1500:
        print("1250")
    elif engine <2000:
        print("2200")
    else:
        print("1400")
elif year >=2000:
    if engine <=1500:
        print("1000")
    elif engine <2000:
        print("1500")
    else:
        print("1200")
else
    if engine <=1500:
        print("1100")
    elif engine <2000:
        print("1700")
    else:
        print("1300")
