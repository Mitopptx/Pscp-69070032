"""this femboy taller than other"""
def main():
    """:3"""
    n,l=map(int,input().split())
    narr=list(map(int,input().split()))
    larr = list(map(int,input().split()))
    j=0
    arr= []
    for i in range(n):
        arr.append(narr[i])
        if larr[j] ==i+1:
            if max(arr) == arr[i] or i==0:
                t =0
                for k in range(len(arr)-1):
                    if  arr[k] == max(arr):
                        t = 1
                print(t)
            else:
                print(max(arr)-arr[i]+1)
            j+=1
main()
