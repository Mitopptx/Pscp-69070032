"""Bus"""
def main():
    """ahhhh"""
    row = int(input())
    col = int(input())
    sit = int(input())
    for i in range(row, 0, -1):
        for j in range(col):
            place = (row * j) + i
            if j == col - 1:
                if place == sit:
                    print("XX")
                else:
                    print(f"{place:02d}")
            else:
                if place == sit:
                    print("XX", end=" ")
                else:
                    print(f"{place:02d}", end=" ")
        if i % 2 and i != 1:
            print()
main()
