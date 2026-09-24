"""LIGHT BRUH"""
def main():
    """:3"""
    n = int(input())
    number = [0]*n
    for i in range(n):
        num = int(input())
        number[i] = num
    number = sorted(number)
    total = 0
    num = 0
    for i in number:
        num += i
        total += num*2
    print(total)
main()
