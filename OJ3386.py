"""Dopleganger"""
def main():
    """:3"""
    m = int(input())
    n = int(input())
    g1 = [0]*m
    g2 = [0]*n
    num=[]
    for i in range(m):
        g1[i] = int(input())
    for i in range(n):
        g2[i] = int(input())
    for i in range(m):
        for j in range(n):
            if g1[i] ==g2[j]:
                num.append(g1[i])
    num.sort()
    if num:
        for i in num:
            print(i)
    else:
        print("nope")
main()
