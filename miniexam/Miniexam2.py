"""miniexam"""
def main():
    """:3"""
    mem =[]
    while True:
        word = input()
        if word == ("End"):
            break
        if word == "Sorry":
            mem.remove(mem[-1])
        else:
            mem.append(word)
    for i in mem:
        print(i,end="")
        if i != mem[-1]:
            print(", ",end="")
main()
