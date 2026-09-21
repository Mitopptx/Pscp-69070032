"""raBBit"""
def main():
    """o-o"""
    word = input().upper()
    macount = 0
    count = 0
    has_ra = False
    has_b = False
    for i, _ in enumerate(word):
        if word[i] == "R":
            if i + 1 >= len(word) or word[i+1] != "A":
                print("no", i)
                return
            has_ra = True
            count = 0
        elif word[i] == "A":
            if not i or word[i-1] not in ("R", "A"):
                print("no", i)
                return
            count += 1
            macount = max(macount, count)
        elif word[i] == "B":
            if i + 1 >= len(word) or word[i+1] not in ("I", "T"):
                print("no", i+1)
                return
            has_b = True
            count = 0
        elif word[i] in ("I", "T"):
            count = 0
        else:
            print("no", i)
            return
    if has_ra or has_b:
        print("yes", macount)
    else:
        print("unknown", len(word))
main()
