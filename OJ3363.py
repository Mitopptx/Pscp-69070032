"""fluu"""
def main():
    """time flu"""
    n1,n2= map(int,input().split())
    xa,ya=map(int,input().split())
    time = int(input())
    x=[0]*time
    y=[0]*time
    count =0
    for i in range(time):
        x[i],y[i] = map(int,input().split())
    for i in range(n1):
        for j in range(n2):
            temp = False
            for k in range(time):
                if (abs(i-x[k])<=2)and (abs(j-y[k])<=2):
                    temp =True
                    break
            if temp is False:
                count+=1
    print(count)
    per=0
    maper = 0
    for i in range(time):
        if xa == x[i] and ya == y[i]:
            per=100
        elif abs(xa-x[i])<=1 and abs(ya-y[i])<=1:
            per = 60
        elif abs(xa-x[i])<=2 and abs(ya-y[i])<=2:
            per = 20
        else:
            per = 0
        if maper < per:
            maper = per
    print(maper,end="%")
main()
