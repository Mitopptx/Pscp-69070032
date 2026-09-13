"""Bread bood"""
def main():
    """o-o"""
    w,h,m,n = map(int,input().split())
    XM = list(map(int,input().split()))
    YN = list(map(int,input().split()))
    X=[]
    Y=[]
    for i in range(m+1):
        if not i:
            X.append(XM[i])
        elif i == m:
            X.append(w-XM[i-1])
        else:
            X.append(XM[i]-XM[i-1])
    for i in range(n+1):
        if not i:
            Y.append(YN[i])
        elif i == n:
            Y.append(h-YN[i-1])
        else:
            Y.append(YN[i]-YN[i-1])
    total =[]
    for i in range(m+1):
        for j in range(n+1):
            total.append(X[i]*Y[j])
    ma1 = max(total)
    total.pop(total.index(ma1))
    ma2 = max(total)
    print(ma1,ma2)
main()
