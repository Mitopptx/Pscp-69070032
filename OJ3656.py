"""kang"""
def main():
    """:3"""
    num = input()
    total =0
    for i in num :
        total += int(i)
    two = int(num[10:])*10
    total += two
    if total<1000:
        total+=1000
    if len(str(total))>4:
        total = str(total)
        print(total[-4:])
    else:
        print(total)
main()
