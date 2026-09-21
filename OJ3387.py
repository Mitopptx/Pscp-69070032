"""depress tuple"""
def main():
    """:3"""
    tup = tuple(map(str,input().split()))
    x = input()
    position = tup.index(x)
    amount = tup.count(x)
    for _ in range(amount):
        for i in range(amount):
            print(str(position),end="")
            if i != amount-1:
                print(end=" ")
        print()
main()
