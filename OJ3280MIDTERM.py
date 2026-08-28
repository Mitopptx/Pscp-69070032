"""code cleaser"""
def main():
    """kai cleaner"""
    word = input()
    new = ""
    letter = 0
    digit = 0
    temp = 0
    for a in word.split(" "):
        if a.isalpha():
            new += a.upper()
            letter += len(a)
        elif a.isdigit():
            new += a
            digit += len(a)
        else:
            for i in a:
                if i.isalpha():
                    new += i.upper()
                    letter += len(i)
                elif i.isdigit():
                    new += i
                    digit += len(i)
        new += " "
    if not letter and not digit:
        print("CODE = NONE\nLETTERS = 0\nDIGITS = 0")
    else:
        print("CODE = ",new.strip().replace(' ','-'))
        print("LETTERS =",letter)
        print("DIGITS =",digit)
main()
