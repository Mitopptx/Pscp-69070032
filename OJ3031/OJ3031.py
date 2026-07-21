"""INK WARANTORN"""
import math
s,n = map(int,input().split())
total={}
for i in range(n):
    x,y = map(int,input().split())
    c = math.sqrt((x**2)+(y**2))
    total[i] = (c**2)*3.1416 /s
for i in range(n):
    print(math.ceil(total[i]))
