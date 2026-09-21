"""picknum"""
def main():
    """:3"""
    num = list(map(int,input().split()))
    pos =0
    neg =0
    zero = 0
    for i in num:
        if i >0:
            pos +=1
        elif i < 0:
            neg +=1
        elif not i:
            zero += 1
    print("Positive: ",pos,"\nNegative: ",neg,"\nZero: ",zero,sep="")
main()
