"""miniexam"""
def main():
    """:3"""
    mem =[]
    while True:
        word = input().lower()
        if "cat" in word:
            mem.append(word)
        if word == ("-1"):
            break
    print("The number of cat in bag",len(mem))
    print("List of cat",mem)
main()
