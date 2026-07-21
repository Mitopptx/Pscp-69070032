"""Break the 4 wall"""
room = int(input())
i=1
floor = 0
while i>0:
    low = ((i-1)**2)+1
    high = i**2
    if low<= room <= high:
        floor = i
        i = -1
    i+=1
if not floor%2:
    if not room%2:
        print((floor-1)*2)
    else:
        print(((floor-1)*2)-1)
else:
    if not room%2:
        print(((floor-1)*2)-1)
    else:
        print((floor-1)*2)
