"""this femboy taller than other"""
def main():
    """:3"""
    _, _ = map(int, input().split())
    height = list(map(int, input().split()))
    customer = list(map(int, input().split()))
    for pos in customer:
        if pos == 1:
            print(0)
            continue
        max_height = 0
        for i in range(pos - 1):
            if height[i] > max_height:
                max_height = height[i]
        if height[pos - 1] >= max_height:
            print(0)
        else:
            print(max_height - height[pos - 1] + 1)
main()
