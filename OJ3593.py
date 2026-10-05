"""febuaryrecursive"""
def main():
    """:3"""
    n = int(input())
    arr = []
    recur(n,arr)
def recur(n,arr):
    """Recur"""
    if n > len(arr):
        if not n:
            return 0,arr
        if n==1:
            return 1,arr
    else: 
    return recur(n-1,arr) + recur(n-2,arr)
main()
