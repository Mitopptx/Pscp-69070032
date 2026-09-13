"""number disorder"""
def main():
    """o-o"""
    num = -2
    number = []
    short=""
    while num != -1:
        num = int(input())
        number.append(num)
    temp=0
    for i in range(len(number)-1):
        if i==len(number)-2:
            short+=str(number[i])
        elif number[i]+1==number[i+1]:
            if not temp:
                short+= str(number[i])+"-"
                temp=1
        else:
            short += str(number[i])+", "
            temp=0
    print(short)
main()
