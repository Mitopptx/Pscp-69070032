"""another rabbit"""
def main():
    """clank clank labubu"""
    s = input()
    temp = -10
    count = -10
    for i in s:
        if i in("b","B"):
            if temp < count:
                temp = count
            count=0
        elif i in("u","U"):
            count+=1
    if temp > count:
        count = temp
    if count>=2:
        print("Yes",count)
    elif count<2 and count>=0:
        temp1=0
        for i in s:
            if temp1==1:
                print("U",end="")
            elif i in("b","B"):
                print("B",end="")
                temp1=1
            else:
                print(i,end="")
    else:
        area = int(len(s)/3)
        r = len(s)-(area*3)
        print("BUU"*area,end="")
        if r ==1:
            print("B")
        elif r == 2:
            print("BU")
main()
