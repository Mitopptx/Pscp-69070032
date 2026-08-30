"""box of scrap"""
def main():
    """Tony stark able to build this"""
    W,L,M,N= map(int,input().split())
    maxwaste = 1000000
    for A in range(M,N+1):
        remain = L % A
        area = W * remain
        space = remain // 1 * (W // A)
        waste = area - space * A
        if maxwaste> waste:
            maxwaste = waste
    print(maxwaste)
main()
