"""Caesar cipher"""
def main():
    """:3"""
    word = input()
    start = (word.split())[0]
    num = 1
    check = ""
    while num<=26:
        for i in start:
            if (i.isupper() and (ord(i)-num)<65 ) or (i.islower() and (ord(i)-num)<97):
                check += chr(ord(i)+26-num)
            else:
                check += chr(ord(i)-num)
        if check.lower() in ("what", "when", "why", "which", "this",
                     "there", "where", "the", "is", "am",
                     "are", "you", "we", "they", "he", "she", "it"):
            break
        num += 1
        check = ""
    for i in word:
        if i.isalpha() and ((i.isupper() and ord(i)-num < 65) or
            (i.islower() and ord(i)-num < 97)):
            print(chr(ord(i)+26-num), end="")
        elif i.isalpha():
            print(chr(ord(i)-num), end="")
        else:
            print(i, end="")
main()
