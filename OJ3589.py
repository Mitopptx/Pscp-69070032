"""febuaryrecursive"""
def main():
    """:3"""
    n = int(input())
    print(fibonacci(n))
def fibonacci(n):
    """febu"""
    if not n:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
main()
