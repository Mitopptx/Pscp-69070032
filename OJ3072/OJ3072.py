"""SQUID GAME"""
st = input()
arr = [0,0,0,0,0]
for z in st:
    if z in ('a', 'A'):
        arr[0]+=1
    elif z in('e', 'E'):
        arr[1]+=1
    elif z in('i','I'):
        arr[2]+=1
    elif z in('o', 'O'):
        arr[3]+=1
    elif z in('u', 'U'):
        arr[4]+=1
if  arr[0]>0:
    print("a :",arr[0])
if arr[1]>0:
    print("e :",arr[1])
if arr[2]>0:
    print("i :",arr[2])
if arr[3]>0:
    print("o :",arr[3])
if arr[4]>0:
    print("u :",arr[4])
