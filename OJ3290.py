"""Larrow"""
def main():
    """Arrow"""
    k = int(input())
    n = int(input())
    for i in range(1,n+1):
            print(" "*(n-i),end="")
            print("*"*k)
    for i in range(1,n):
            print(" "*(i),end="")
            print("*"*k)
main()
