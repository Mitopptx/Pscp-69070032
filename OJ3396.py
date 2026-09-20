"""fastest black people"""
def main():
    """:3"""
    n,k=map(int,input().split())
    arr=[0]*n
    for i in range(n):
        arr[i] = int(input())
    fastest = min(arr)
    count=0
    for i in range(n):
        if fastest*k < arr[i]*(k-1):
            count +=1
    print(count)
main()
