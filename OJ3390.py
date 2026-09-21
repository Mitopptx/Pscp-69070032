"""ARRAY 4DX"""
def main():
    """:3"""
    one=list(map(int,input().split()))
    two=list(map(int,input().split()))
    three=list(map(int,input().split()))
    four=list(map(int,input().split()))
    five=list(map(int,input().split()))
    first =-1
    secound = -1
    if sum(one)%2:
        first = 0
    elif sum(two)%2:
        first = 1
    elif sum(three)%2:
        first = 2
    elif sum(four)%2:
        first = 3
    elif sum(five)%2:
        first = 4
    for i in range(5):
        if (one[i]+two[i]+three[i]+four[i]+five[i]) %2:
            secound = i
            break
    print(first,secound)
main()
