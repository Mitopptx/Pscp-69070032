"""pass or not not what I care"""
n = int(input())
avg = 0
check = 0
for n in range(n):
    num = int(input())
    if num <50:
        check = -1
    avg += num
avg /= n+1
if check ==-1 or avg <60:
    print(f"{avg:.1f}","\nFAIL",sep="")
else:
    print(f"{avg:.1f}","\nPASS",sep="")
