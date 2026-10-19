"""balling"""
def main():
    """:3"""
    n = int(input())
    price =0
    weight = 0
    mem = 0
    for _ in range(n):
        p = float(input())
        w = float(input())
        memo = w/p
        if mem<memo:
            mem = memo
            price = p
            weight = w
    print(f"{price:.2f} {weight:.2f}")
main()
