"""br"""
def main():
    """brr"""
    n=int(input())
    text = 0
    if n==1:
        print("1")
    else:
        for i in range(1, 1+n):
            text += len(str(i))+1
        print(text)
main()
