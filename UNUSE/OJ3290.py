"""Larrow"""
def main():
    """Arrow"""
    k = int(input())
    n = int(input())
    for i in range(1,int(n/2)+1):
        print(" "*(int(n/2)-i+1),end="")
        print("*"*k)
    for i in range(int(n/2)+1):
        print(" "*(i),end="")
        print("*"*k)
main()
