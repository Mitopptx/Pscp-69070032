"""Car"""
def main():
    """o-o"""
    n = int(input())
    arr=[0]*n
    count=0
    for i in range(n):
        unuse,engine= map(int,input().split())
        arr[i] = engine
        if not i:
            continue
        elif arr[i-1]<engine:
            count +=1
    print(count)
main()
