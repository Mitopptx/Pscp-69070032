"""soiting port"""
def main():
    """wher's the sauce"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        x=[0]*n
        y=[0]*n
        arr = [0]*n
        for i in range(n):
            x[i],y[i]= map(int,input().split())
            arr[i] = x[i]+y[i]
        newx,newy = sortedxy(arr,x,y)
        for i in range(n):
            print(newx[i],newy[i])
def sortedxy(arr,x,y):
    """sortedxy"""
    n= len(arr)
    newarr=[0]*n
    newx=[0]*n
    newy=[0]*n
    for i in range(n):
        newarr[i] = min(arr)
        indexx = arr.index(min(arr))
        newx[i] = x[indexx]
        newy[i] = y[indexx]
        arr.pop(indexx)
        x.pop(indexx)
        y.pop(indexx)
        if newarr[i-1] ==  newarr[i]:
            for j in range (i,0,-1):
                 if newarr[j] == newarr[j-1]:
                     temp=0
                     if newy[j] > newy[j-1]:
                         temp = newy[j-1]
                         newy[j-1] = newy[j]
                         newy[j] = temp
                         temp = newx[j-1]
                         newx[j-1] = newx[j]
                         newx[j] = temp
    return(newx,newy)
main()
