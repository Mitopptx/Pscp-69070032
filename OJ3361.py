"""Car"""
def main():
    """o-o"""
    n = int(input())
    arr=[0]*n
    count=0
    for i in range(n):
        _,engine= map(int,input().split())
        arr[i] = engine
    for i in range(n-1,-1,-1):
        print(i)
        if max(arr)==arr[i]:
            count += len(arr)-1
            break
        arr.remove(arr[i])
    print(count)
main()
