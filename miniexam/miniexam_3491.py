"""Run Game"""
def main():
    """:3"""  
    try:
        num = list(map(int, input().split()))
    except EOFError:
        num = []
    count =0
    current = 0
    for i in num:
        count += abs((i-current))
        current = i
    print(count)
main()
