"""kang"""
def main():
    """:3"""
    l1 = input().strip("[]")
    l1 = list(map(int,l1.split(", ")))
    l2 = input().strip("[]")
    l2 = list(map(int,l2.split(", ")))
    n = int(input())
    if len(l1) > len(l2):
        lus = l2.copy()
        lcompare = l1.copy()
    else:
        lus = l1.copy()
        lcompare = l2.copy()
    lus = sorted(lus)
    luse = []
    for i in lus:
        if i <= n:
            luse.append(i)
        else:
            break
    count =0
    for i in luse:
        if n-i in lcompare:
            count+=1
    print(count)
main()
