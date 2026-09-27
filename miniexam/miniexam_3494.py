"""Icecream"""
def main():
    """:3"""
    alice = int(input())
    bob = int(input())
    seller = int(input())
    dis1 = abs(seller - alice)
    dis2 = abs(seller - bob)
    if dis1<dis2:
        print("Alice",dis1)
    elif dis2<dis1:
        print("Bob",dis2)
    else:
        print("Sundaes",abs(seller-alice))
main()
