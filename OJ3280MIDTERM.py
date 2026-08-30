"""code cleaner"""
def main():
    """kai cleaner"""
    word = input()
    new = ""
    letter = 0
    digit = 0
    for a in word:
        if a.isalpha():
            new += a.upper()
            letter += 1
        elif a.isdigit():
            new += a
            digit += 1
        else:
            if new and new[-1] != "-":
                new += "-"
    new= new.strip("-")
    if new == "":
        new = "NONE"
    print("CODE =", new)
    print("LETTERS =", letter)
    print("DIGITS =", digit)
main()
