"""num miss"""
def main():
    """:3"""
    n = int(input())
    number = set()
    while True:
        num = int(input())
        if not num:
            break
        number.add(num)
    for i in range(1,n+1):
        if i not in number:
            print(i)
main()
