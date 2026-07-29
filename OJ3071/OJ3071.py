"""wat is this q?"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())
count=0
for a in range(a,b+1):
    if a%d==r:
        count+=1
print(count)
