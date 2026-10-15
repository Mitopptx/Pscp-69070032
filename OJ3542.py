"""Calcarlo"""
def main():
    """:3"""
    n = int(input())
    count = n - 1
    start = 1
    digits = 1
    while start <= n:
        end = min(n, start * 10 - 1)
        count += (end - start + 1) * digits
        start *= 10
        digits += 1
    if n > 1:
        count += 1
    print(count)
main()
