"""kang"""
def main():
    """:3"""
    money = int(input())
    n = int(input())
    if money<n:
        print("-1")
        return
    if money%8 ==4:
        total = (money //8 )-1
    else:
        total = money //8
    print(total)
main()
