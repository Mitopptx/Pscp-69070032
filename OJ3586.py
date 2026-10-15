"""KABABABAAB"""
def main():
    """:3"""
    n =int(input())
    for _ in range(n):
        word = input()
        i = 0
        while i < len(word):
            check = True
            if word[i:i+5] == "bakka":
                i+=5
                continue
            if word[i:i+4] == "baka":
                check = False
                break
            if word[i:i+2] in ("ta","ka","ba"):
                i+=2
                continue
            check = False
            break
        if check:
            print("yes")
        else:
            print("no")
main()
