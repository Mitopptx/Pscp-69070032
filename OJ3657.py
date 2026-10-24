"""kang"""
def main():
    """:3"""
    ans = input()
    gue = input()
    nans = ""
    ngue = ""
    count=0
    for i in range(len(ans)):
        if ans[i] == gue[i]:
            print("B",end="")
            count+=1
        else:
            nans += ans[i]
            ngue += gue[i]
    for i in nans:
        if i in ngue:
            print("W",end="")
            count+=1
    print("O"*(4-count))
main()
