"""Coffee 3 friend"""
day = int(input())
low = 9999999999999
high = 0
total = 0
for day in range(day):
    num = int(input())
    if low > num:
        low = num
    if high < num:
        high = num
    total += num
print(total,high,low,round(total/(day+1),1),sep="\n")
