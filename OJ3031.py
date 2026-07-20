"""INK WARANTORN"""
import math
s,n = map(int,input().split())
r = math.sqrt(s/3.1416)
far={}
for i in range(n):
    x,y = map(int,input().split())
    far[i] = math.sqrt((x**2)+(y**2))
for i in range(n):
    print(math.ceil(far[i]/r))
