"""rabbit fatfuck"""
count = 0
temp = 0
name = ""
n = int(input())
for n in range(n):
    rabbit,weight= map(str,input().split())
    weight = int(weight)
    if weight > temp:
        name = rabbit
        temp = weight
    if weight> 15:
        count +=1
print(count)
print(name)
