"""NO PAIR"""
def main():
    """:4"""
    word = input()
    mem = ""
    for i in word:
        if word.count(i) % 2 == 1 and i not in mem:
            mem += i
    if mem:
        print(mem)
    else:
        print("fully paired")
main()
