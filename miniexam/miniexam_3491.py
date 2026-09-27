"""Run Game"""
def main():
    """:3"""
    num = list(map(int,input().split()))
    count =0
    current = 0
    for i in num:
        count += abs((i-current))
        current = i
    print(count)
main()
