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
        count = 0
        for j in stat[i]:
            count+=1
            if not j:
                count -=1
        print(count,sum(stat[i]))
    """ for i in range(n):
        row = stat[i]
        
        count = 0
        for j in row:
            count+=1
            if not j:
                count -=1
            print(j,end=" ")
        print(count,sum(row))"""

main()
