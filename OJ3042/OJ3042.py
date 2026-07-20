"""div 10"""
n = int(input())
while n>=0:
    if not n%10:
        print(n,end=' ')
        n-=10
    else:
        n-=1
