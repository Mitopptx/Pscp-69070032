"""Bullet"""
def main():
    """:3"""
    n =int(input())
    data=[]
    for _ in range(n):
        x,y,d = map(int, input().split())
        data.append((x, y, d))
    for tx in range(1000):
        for ty in range(1000):
            correct = True
            for x, y, d in data:
                if (tx - x) ** 2 + (ty - y) ** 2 != d ** 2:
                    correct = False
                    break
            if correct:
                print(tx, ty)
                return
main()
