"""Caesar cipher"""
def main():
    """:3"""
    word = input()
    start = (word.split())[0]
    num = 1
    check = ""
    while True:
        for i in start:
            if (i.isupper() and (ord(i)-num)<65 ) or (i.islower() and (ord(i)-num)<97):
                check += chr(ord(i)+26-num)
            else:
                check += chr(ord(i)-num)
        if check in("What", "When", "Why", "Which", "This", "There", "Where", "The", "Is", "Am",
                    "Are", "You", "We", "They", "He", "She", "It"):
            break
        num += 1
        check = ""
    for i in word:
        if i in(" ","."):
            print(i,end="")
        elif (i.isupper() and (ord(i)-num)<65 ) or (i.islower() and (ord(i)-num)<97):
            print(chr(ord(i)+26-num),end="")
        else:
            print(chr(ord(i)-num),end="")
main()
