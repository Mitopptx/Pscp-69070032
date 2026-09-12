"""pick"""
def main():
    """puss in boot"""
    num = list(map(int,input().split()))
    temp = 0
    for i in range(len(num)-1,-1,-1):
        if not num[i]%3 or not num[i]%5:
            print(num[i],end=" ")
            temp= 1
    if not temp:
        print("Nope")
main()
