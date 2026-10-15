"""OPTIMUS PRIME"""
def main():
    """:3"""
    n = int(input())
    if n <2:
        print("NO")
        return
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            print("NO")
            return
    print("YES")
main()
