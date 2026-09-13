"""sorted"""
def main():
    """o-o"""
    arr = []
    for i in range(1,4):
        n = int(input())
        print("Input number",i,"stored.")
        arr.append(n)
    inpu = -1
    while inpu:
        inpu= int(input())
        if inpu ==1:
            print("Original order:",str(arr).strip("[").strip("]").replace(",",""))
        elif inpu ==2:
            print("Descending order:",str(sorted(arr,reverse=True))
            .strip("[").strip("]").replace(",",""))
        elif inpu ==3:
            print("Ascending order:",str(sorted(arr)).strip("[").strip("]").replace(",",""))
main()
