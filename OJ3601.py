"""key card"""
def main():
    """:3"""
    boy = 0
    girl = 0
    while True:
        num = input()
        if num[0] == "-":
            break
        if not int(num[-1])%2:
            girl +=1
        else:
            boy += 1
    print(boy,girl,boy+girl)
main()
