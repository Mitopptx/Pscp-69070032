"""gift and thief"""
N,K,T=map(int,input().split())
count=0
i=0
while i not in (1,T):
    if not count:
        i=1
    i += K
    if i > N:
        i -= N
    count +=1
    if i==T:
        count +=1
if T==1:
    count =1
print(count)
