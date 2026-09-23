"""wat"""
def main():
    """:3"""
    word = input()
    mem = {}
    for i in word:
        if i ==" ":
            continue
        if i in mem:
            mem[i] += 1
        else:
            mem[i] =1
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in mem:
            print(i, "=", mem[i])
        if i.upper() in mem:
            print(i.upper(), "=", mem[i.upper()])
main()
