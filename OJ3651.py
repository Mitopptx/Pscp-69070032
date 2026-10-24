"""kang"""
def main():
    """:3"""
    while True:
        num = input()
        if num == "0":
            break
        while len(num)>1:
            new =0
            for i in num:
                new += int(i)
            num = str(new)
        print(num)
main()
