"""TIRE NO TILE"""
def main():
    """:3"""
    n,p = map(int,input().split())
    stat = [[0]*n]*n
    row = [0]*n
    col = [0]*n
    mem = [0]*n
    for i in range(n):
        stat[i] = list(map(int,input().split()))
    for i in range(n):
        row = stat[i]
        count =0
        k=0
        for j in row:
            print(j,end=" ")
            col[k] += j
            k+=1
            if j:
                count+=1
                mem[k] += 1
        print(count,sum(row))
    for i in mem:
        print(i,end=" ")
    print()
    for i in col:
        print(i,end=" ")
    print()
    print(f"{sum(mem)} {sum(col)} {sum(col)*p:.2f}")
main()
