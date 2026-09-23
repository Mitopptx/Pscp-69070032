"""lod shong"""
def main():
    """:3"""
    Range,n = map(int,input().split())
    start = [0]*n
    stop = [0]*n
    for i in range(n):
        start[i],stop[i] = map(int,input().split())
    macount = 0
    for i in range(1,(Range+1)*2,1):
        count = 0
        for j in range(n):
            if i/2 < stop[j] and i/2>start[j]:
                count +=1
        if macount<count:
            macount = count
    print(macount)
main()
