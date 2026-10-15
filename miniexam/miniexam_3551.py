"""DORA NUK RADOR"""
def main():
    """:3"""
    word = input()
    if word == "Empty":
        item = []
    else:
        item = list(word.split(","))
    word = input()
    if word == "Stone":
        print("I don't need this!")
    else:
        count = 0
        for _ in item:
            count += 1
        if count ==5:
            item.pop(0)
        item.append(word)
    print(item)
main()
