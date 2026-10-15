"""OPTUS Prime"""
def main():
    """:3"""
    n = int(input())
    prime = [True] * (n + 1)
    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    if not prime[n]:
        print("No")
    else:
        print("Yes")
        print(*[i for i in range(2, n + 1) if prime[i]])
main()
