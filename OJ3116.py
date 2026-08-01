name = input()
name = name.upper()
first = ord(name[0])
last = ord(name[-1])
arr = [0]*10
for i in range(10):
    if not (i+1) %2:
        arr[i] = (last - i)%len(name)
    else:
        arr[i]  = (first + i)%len(name)
    if arr[i] >9:
        arr[i] %=10
    if 2<=i<8:
        print(arr[i],end=' ')
