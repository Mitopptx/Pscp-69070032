"""miniexam"""
def main():
    """:3"""
    name = list(input().lower().split())
    word = input()
    if word.lower() in name:
        print(word,"is in the list")
    else:
        print(word,"is not in the list")
main()
