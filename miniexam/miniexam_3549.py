"""miniexam"""
def main():
    """:3"""
    name = list(input().split())
    word = input()
    if word in name:
        name.remove(word)
        print(*name)
    else:
        print("There are no book with that name on this shelf")
main()
