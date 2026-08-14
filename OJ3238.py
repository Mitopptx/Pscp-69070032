"""This is elon mask"""
n,ch = map(str,input().split())
n=int(n)
for i in range(n):
    for j in range(n):
        if j in (i,n-i-1):
            if ch == "#":
                print("#",end="")
            else:
                temp = chr(int(ord(ch) + abs(i-(n//2))))
                print(temp,end="")
        else:
            print("-",end="")
    print("")
