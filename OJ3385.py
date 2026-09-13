"""buss stop"""
def main():
    """o-o"""
    _ = int(input())
    stop = int(input())
    arr =[]
    bus = []
    count =0
    for i in range(1,stop+1):
        arr = list(map(int,input().split()))
        for j in range(1,len(arr)):
            if arr[j]>i and len(bus)<5:
                bus.append(arr[j])
        count += bus.count(i+1)
        bus = [j for j in bus if j!=i+1]
    print(count)
main()
