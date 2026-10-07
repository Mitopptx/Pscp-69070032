"""flat"""
def main():
    """:3"""
    word = input()
    number = []
    num = ""
    for i,_ in enumerate (word):
        if word[i].isdigit() or word[i] == "-":
            num += word[i]
        elif word[i] in (",","]") and num:
            number.append(int(num))
            num = ""
    number = sorted(number,reverse=True)
    print("[",end="")
    print(*number,sep = ", ",end = "]")
main()
