"""SARA ARAIWA"""
N = int(input())
count =0
for N in range(N):
    cha = input()
    if cha in ("a","A","e","E","i","I","o","O","u","U"):
        count += 1
print(count)
