"""code cleaser"""
def main():
    """kai cleaner"""
    word = input()
    new = ""
    letter = 0
    digit = 0
    for a in word.split(" "):
        if a.isalpha():
            new += a.upper()+"-"
            letter += len(a)
        elif a.isdigit():
            new += a+"-"
            digit += len(a)
        else:
            news = ""
            for i in a:
                if i.isalpha():
                    news += i.upper()
                    letter += len(i)
                elif i.isdigit():
                    news += i
                    digit += len(i)
            if news:
                new += news+"-"
    if not letter and not digit:
        print("CODE = NONE\nLETTERS = 0\nDIGITS = 0")
    else:
        print("CODE =",new[:-1])
        print("LETTERS =",letter)
        print("DIGITS =",digit)
main()
