"""stardewvalley"""
def main():
    """murakami"""
    L,N = map(int,input().split())
    count = 1
    mult = startarea(L)-1
    place=mult+1
    while N > place:
        mult += L**2
        place += mult+1
        count+=1
    print(count)
def startarea(l):
    """only monkey can understand this"""
    if not l:
        return 0
    return startarea(l-1)+l
main()
