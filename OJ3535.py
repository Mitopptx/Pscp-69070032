"""classify"""
def main():
    """:3"""
    mem = {}
    while True:
        num = input()
        if num == "END":
            break
        if num[:4] not in mem:
            mem[num[:4]] = 1
        else:
            mem[num[:4]] += 1
    mem = dict(sorted(mem.items()))
    last = 0
    for i in mem:
        if last == i[:2]:
            print("--",end=" ")
        else:
            print(i[:2],end=" ")
            last = i[:2]
        print(int(i[2:5]),mem[i])
main()
