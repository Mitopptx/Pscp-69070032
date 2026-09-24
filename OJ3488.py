"""ROLLER IN DEPP"""
def main():
    """:3"""
    n = int(input())
    light = [False] * 360
    for _ in range(n):
        a, b = map(int,input().split())
        if a < b:
            for i in range(a,b):
                light[i] = True
        else:
            for i in range(a,360):
                light[i] = True
            for i in range(0, b):
                light[i] = True
    if all(light):
        print(360)
        return
    matotal = 0
    total = 0
    for i in range(360):
        if light[i]:
            total += 1
            matotal = max(matotal, total)
        else:
            total = 0
    left = 0
    while left < 360 and light[left]:
        left += 1
    right = 359
    while right >= 0 and light[right]:
        right -= 1
    matotal = max(matotal, left + (359 - right))
    print(matotal)
main()
