"""box of scrap"""
def main():
    """Tony stark able to build this"""
    W,L,M,N= map(int,input().split())
    s=[]
    for A in range(M,N+1):
        remain = L % A
        area = W * remain
        space = remain // 1 * (W // A)
        waste = area - space * A
        s.append(waste)
    print(min(s))
main()
