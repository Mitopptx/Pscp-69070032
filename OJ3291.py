"""Rarrow"""
def main():
    """arrow"""
    k = int(input())
    n = int(input())
    midle = int(n/2)+1
    for i in range(1,n+1):
        for j in range(k):
            if midle >= abs(j-i):
                print(" ",end="")
        print("*"*k)
main()
