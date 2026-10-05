"""align"""
def main():
    """:3"""
    size = int(input())
    allign = input()
    word = input()
    size -= len(word)
    if allign == "left":
        print(word," "*size,sep="")
    elif allign == "right":
        print(" "*size,word,sep="")
    else:
        if not size %2:
            size //= 2
            print(" "*size,word," "*size,sep="")
        else:
            size //= 2
            print(" "*(size+1),word," "*size,sep="")
main()
