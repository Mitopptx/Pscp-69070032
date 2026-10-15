"""Dartvader"""
def main():
    """:3"""
    n = int(input())
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        d = x*x + y*y
        if d <= 4:
            score += 5
        elif d <= 16:
            score += 4
        elif d <= 36:
            score += 3
        elif d <= 64:
            score += 2
        elif d <= 100:
            score += 1
    print(score)
main()
