"""diff"""
def main():
    """o-o"""
    n = int(input())
    m = int(input())
    set1 = set()
    for _ in range(n):
        num = int(input())
        set1.add(num)
    for _ in range(m):
        num = int(input())
        if num in set1:
            set1.remove(num)
    print(*sorted(set1))
main()
