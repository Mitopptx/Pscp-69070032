"""med"""
def main():
    """:3"""
    a = list(map(float,input().split(", ")))
    a.sort()
    n = len(a)
    if not n %2:
        med = (a[n//2] + a[(n//2)-1]) / 2
    else:
        med = a[(n//2)]
    print(f"{med:.2f}")
main()
