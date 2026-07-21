"""LINE MAN MAI KEAW"""
n,k = map(int,input().split())
lnum =[0]*k
for i in range(n):
    number = int(input())
    for j in range(k+1):
        if number == j:
            lnum[j-1]+=1
            break
        j+=1
    i+=1
lnum = [each - min(lnum) for each in lnum]
print(sum(lnum))
