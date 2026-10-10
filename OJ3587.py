"""recurshit"""
def main():
    """:3"""
    n = int (input())
    print(recur(n))
def recur(n):
    """recurs"""
    if n == 1:
        return "1"
    if n== 2:
        return "2"
    return recur(n-1) + recur(n-2)
main()
