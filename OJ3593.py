"""febuaryrecursive"""
def main():
    """:3"""
    n = int(input())
    arr = []
    recur(n,arr)
    n = int(input())
    print(fibonacci(n)[0])
def fibonacci(n):
    if n == 0:
        return (0, 1)
    a, b = fibonacci(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, c + d)
main()
