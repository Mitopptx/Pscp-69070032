"""antique"""
def main():
    """:3"""
    _ = int(input())
    num = list(map(int,input().split()))
    check = []
    dup = set()
    for i in num:
        if i in check:
            dup.add(i)
        else:
            check.append(i)
    for i in dup:
        if i in check:
            check.remove(i)
    check = sorted(check)
    for i in check:
        print(i,end=" ")
main()
