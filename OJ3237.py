"""0traingle"""
n = int(input())
for i in range(n):
    for j in range(i+1):
        if not j or i==n-1:
            print(0,end="")
        elif j == i:
            print(0,end="")
        else:
            print(1,end="")
    print("")
