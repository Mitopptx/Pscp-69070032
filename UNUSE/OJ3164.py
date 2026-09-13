"""plus ultra"""
n = int(input())
arr = [0]*n
s=0
for i in range(n):
    num1 = int(input())
    num2 = int(input())
    if num1>num2:
        arr[i]=num1
    else:
        arr[i]=num2
for i in range(n):
    if n==1:
        s=0
    elif i ==n-1:
        print(arr[i],"=",end=" ")
    else:
        print(arr[i],"+",end=" ")
    s += arr[i]
print(s)
