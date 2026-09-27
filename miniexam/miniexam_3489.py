"""miniexam"""
def main():
    """mini"""
    n = int(input())
    number =0
    for i in range (n+1):
        if not i%3 or not i %5:
            number += i
    print(number)
main()
