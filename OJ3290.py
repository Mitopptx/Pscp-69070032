"""Larrow"""
def main():
    """Arrow"""
    k = int(input())
    n = int(input())
    midle = int(n/2)+1
    for i in range(1,n+1):
        for j in range(abs(midle-i)):
            if i<  midle or i> midle:
                print(" ",end="")
        print("*"*k)
main()
