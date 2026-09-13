"""arrow"""
def main():
    """Arrow"""
    k = input()
    n = int(input())
    for i in k:
        if i == "R":
            rarrow(n)
        else:
            larrow(n)
        print("")
def rarrow(n):
    """Rarrow"""
    for i in range(1,n+1):
        print(" "*((i*2)-2),end="")
        print("*"*(n-i+1))
    for i in range(1,n):
        print(" "*((n*2)-(i*2)-2),end="")
        print("*"*(i+1))
def larrow(n):
    """Larrow"""
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        print("*"*(n-i+1))
    for i in range(1,n):
        print(" "*(i),end="")
        print("*"*(i+1))
main()
