"""Anime last stand"""
def main():
    """tower defence"""
    num = input()
    num = num.strip("[")
    num = num.strip("]")
    number = list(num.split(","))
    for i in number:
        print(int(i)%10)
main()
