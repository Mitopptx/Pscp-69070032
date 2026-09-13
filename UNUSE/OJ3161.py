"""symbol"""
n = int(input())
for n in range(1,n+1):
    if not n%5:
        print("X",end="")
    else:
        print("*",end="")
