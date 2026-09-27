"""tug"""
def main():
    """:3"""
    counta =0
    countb = 0
    for _ in range(10):
        num = int(input())
        counta += num
    for _ in range(10):
        num = int(input())
        countb += num
    if counta > countb:
        print("B")
    elif countb > counta:
        print("A")
    else:
        print("AB")
main()
