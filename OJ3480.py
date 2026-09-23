"""BIRD TUNG CHAI"""
def main():
    """:3"""
    n= int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n):
        if n== 1:
            count = 1
            break
        if not i:
            if arr[i]>arr[i+1]:
                count+=1
        elif i == n-1:
            if arr[i]> arr[i-1]:
                count+=1
        elif arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            count+=1
    print(count)
main()
