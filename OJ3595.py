"""metreostike"""
def main():
    """:3"""
    a = float(input())
    b = int(input())
    c = float(input())
    weight = a
    count = 0
    i = 0
    while weight >= c:
        weight = weight/b
        if not i:
            count += 1
        else:
            count += b**i
        i+=1
    print(count)
main()
