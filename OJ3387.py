"""depress tuple"""
def main():
    """:3"""
    tup = tuple(map(str,input().split()))
    x = input()
    position = tup.index(x)
    amount = tup.count(x)
    for _ in range(amount):
        for _ in range(amount):
            print(str(position),end=" ")
        print()
main()
