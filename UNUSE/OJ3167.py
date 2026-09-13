"""BUZZZZ"""
num = int(input())
for i in range(1,num+1):
    temp=0
    if not i %3:
        print("Fizz",end="")
        temp = 1
    if not i %5:
        print("Buzz",end="")
        temp = 1
    if temp==1:
        print("")
    else:
        print(i)
