"""Car"""
def main():
    """o-o"""
    n = int(input())
    arr=[0]*n
    count=0
    for i in range(n):
        _,engine = map(int,input().split())
        arr[i] = engine
    while len(arr):
        ma = max(arr)
        for i in range(arr.index(ma),-1,-1):
            if not i:
                arr.pop(0)
                break
            count+=1
            arr.pop(i)
    print(count)
main()
