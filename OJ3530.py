"""square"""
def main():
    """:3"""
    n = int(input())
    square_free = [True] * (n + 1)
    square_free[0] = False
    i = 2
    while i * i <= n:
        square = i * i
        for j in range(square, n + 1, square):
            square_free[j] = False
        i += 1
    print(sum(square_free))
main()
