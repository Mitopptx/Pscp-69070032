"""take it or double to the next person"""
def main():
    """:3"""
    n,s = map(int,input().split())
    s-=1
    arr= [0]*n
    check =[-1]*(n+1)
    for i in range(n):
        arr[i] = (int(input()))-1
    loop = True
    i=0
    count=-1
    while loop:
        if s in check or s == -1:
            loop = False
        count +=1
        check[i] = s
        s= arr[s]
        i+=1
    print(count)
main()
