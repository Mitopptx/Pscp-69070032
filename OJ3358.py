"""Pig"""
def main():
    """pigy pie"""
    n = int(input())
    pig = list(map(int,input().split()))
    summ=0
    txt=""
    for i in range(0,n*2,2):
        if pig[i] > pig[i+1]:
            txt += str(pig[i])
            summ += pig[i]
        else:
            txt += str(pig[i+1])
            summ += pig[i+1]
        if i !=(n*2)-2:
            txt +=" + "
    if n == 1:
        print(summ)
    else:
        print(txt,"=",summ)
main()
