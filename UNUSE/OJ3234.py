"""Marry Chrismas!!!"""
ch,n = map(str,input().split())
n = int(n)
for n in range(n):
    if ch =="R":
        print("Red",end=" ")
        ch = "G"
    elif ch =="G":
        print("Green",end=" ")
        ch = "B"
    elif ch =="B":
        print("Blue",end=" ")
        ch = "R"
