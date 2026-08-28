"""midterm exam"""
def main():
    """exam"""
    n = int(input())
    if not n:
        mx = 0
        mn = 0
        avg = 0
    else:
        num = int(input())
        mn = num
        mx = num
        avg = num
        for _ in range(n-1):
            num = int(input())
            if mn >num:
                mn = num
            if mx < num:
                mx = num
            avg += num
    avg = avg/ (n)
    print(f"MIN: {mn:.3f}\nMAX: {mx:.3f}\nAVG: {avg:.3f}")
main()
