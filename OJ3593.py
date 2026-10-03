"""febuaryrecursive"""
def main():
    """:3"""
    n = int(input())
    arr = []
    for i in range(n):
        arr[i]
    recur(n)
def recur(n):
    """Recur"""
    if not n:
        return 0
    if n==1:
        return 1
    return recur(n-1) + recur(n-2)
main()
