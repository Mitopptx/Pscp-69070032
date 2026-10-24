"""kang"""
def main():
    """:3"""
    a = input()
    b = input()
    c = input()
    num = []
    num.append(int(a+b+c))
    num.append(int(a+c+b))
    num.append(int(b+a+c))
    num.append(int(b+c+a))
    num.append(int(c+a+b))
    num.append(int(c+b+a))
    total = num[0]
    for i in num:
        if total<i:
            total = i
    print(total)
main()
