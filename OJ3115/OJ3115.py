"""when it's opne"""
store,check = map(int,input().split())
arrs = [0]*store
for i in range(store):
    arrs[i] = input()
strcheck = input()
timecheck = strcheck.split(" ")
for i in range(check):
    count =0
    for j in range(store):
        start,stop= arrs[j].split()
        if int(start)<= int(timecheck[i]) < int(stop):
            count +=1
    print(count,end=" ")
