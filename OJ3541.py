"""coke keng puy"""
def main():
    """:3"""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    if not b or c>a:
        c=a
        b=1
    need = (d-1)//b
    total = (need * c)+((d-need)*a)
    if not d:
        total = 0
    print(total)
main()
