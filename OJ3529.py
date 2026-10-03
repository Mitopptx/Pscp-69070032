"""Caesar cipher"""
def main():
    """:3"""
    word = input()
    common = ("what", "when", "why", "which", "this",
              "there", "where", "the", "is", "am",
              "are", "you", "we", "they", "he", "she", "it")
    num = 1
    found = False
    while num <= 26:
        check = ""
        for i in word.lower():
            if i.isalpha():
                check += chr((ord(i) - 97 - num) % 26 + 97)
            elif i == " ":
                check += i
        checkin = check.split()
        for i in checkin:
            if i in common:
                found = True
                break
        if found:
            break
        num += 1
    for i in word:
        if i.isupper():
            print(chr((ord(i) - 65 - num) % 26 + 65), end="")
        elif i.islower():
            print(chr((ord(i) - 97 - num) % 26 + 97), end="")
        else:
            print(i, end="")
main()
