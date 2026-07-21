"""DU DU DU MIN...."""
n = int(input())
temp = int(input())
for i in range(n-1):
    num = int(input())
    if num<=temp:
        temp = num
    i+=1
print (temp)
