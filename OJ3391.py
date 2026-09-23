"""MagicCCCC"""
def main():
    """:3"""
    n = int(input())
    fire = 0
    water = 0
    earth = 0
    for _ in range(n):
        f1, w1, e1, f2, w2, e2 = map(int, input().split())
        first = [f1, w1, e1]
        second = [f2, w2, e2]
        if sum(first) >= sum(second):
            fire += f1
            water += w1
            earth += e1
        else:
            fire += f2
            water += w2
            earth += e2
    total = fire + water + earth
    print("Total:", total)
    print("Fire:", fire)
    print("Water:", water)
    print("Earth:", earth)
    if fire > water + earth:
        print("Bonus: YES")
    else:
        print("Bonus: NO")
main()
