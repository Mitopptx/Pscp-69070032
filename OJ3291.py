"""Rarrow"""
def main():
    """Arrow"""
    k = int(input())
    n = int(input())
    for i in range(1,int(n/2)+1):
        print(" "*(i-1),end="")
        print("*"*k)
    for i in range(int(n/2),n):
        print(" "*(n-i-1),end="")
        print("*"*k)
main()
