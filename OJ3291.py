"""Rarrow"""
def main():
    """Arrow"""
    k = int(input())
    n = int(input())
    midle = int(n/2)
    for i in range(n):
        if i<=midle:
            for j in range(i):
                print(" ",end="")
        else:
            for j in range(n-i-1):
                print(" ",end="")
        print("*"*k)
main()
