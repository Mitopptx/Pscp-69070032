"""cave"""
def main():
    """o-o"""
    n= int(input())
    arr = list(map(int,input().split()))
    place = arr.index(1)
    tres = arr.index(2)
    mapp = input()
    for i in mapp:
        if i == "R" and place+1<n:
            place+=1
        elif i == "L" and place-1>=0:
            place-=1
        if place == tres:
            break
    arr = [0]*n
    arr[tres] = 2
    arr[place] = 1
    print(str(arr).strip("[").strip("]").replace(",",""))
main()
