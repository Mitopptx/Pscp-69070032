"""Filterrrrer"""
def main():
    """:3"""
    w = input().strip("{").strip("}")
    fil = float(input())
    wo = list(w.split(", "))
    word = {}
    for i in wo:
        word[i[1:9]] = float(i[12:])
    word = dict(sorted(word.items()))
    temp = False
    for i in word:
        if word[i] >= fil:
            print(i,end="	")
            print(f"{word[i]:.2f}")
            temp = True
    if not temp:
        print('Nope')
main()
