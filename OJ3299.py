"""stardewvalley"""
def main():
    """murakami"""
    L,N = map(int,input().split())
    count = 1
    place = (startArea(L))
    while N > place:
        place += place+(L**2)
        count+=1
    print(count)
def startArea(L):
    """only monkey can understand this"""
    if not L:
        return 0
    else:
        return startArea(L-1)+L-1
main()
