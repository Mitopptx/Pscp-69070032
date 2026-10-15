"""Fibonacci"""
def fibonacci(n):
    """:3"""
    if not n:
        return 0, 1
    a, b = fibonacci(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    if not n % 2:
        return c, d
    return d, c + d
def main():
    """:3"""
    n = int(input())
    print(fibonacci(n)[0])
main()
