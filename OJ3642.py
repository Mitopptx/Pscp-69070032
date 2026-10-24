"""kang"""
def main():
    """:3"""
    xo = [0]*9
    for i in range(3):
        x = input()
        for j in range(3):
            xo[(i*3)+j] = x[j]
    if((xo[0] == xo[1] )and (xo[0] == xo[2])) or ((xo[0] == xo[4]) and (xo[0] ==xo[8])) or ((xo[0] ==xo[3])and (xo[0]==xo[6])):
        print(xo[0],"WIN")
    elif((xo[2] == xo[5] )and (xo[2] == xo[8])) or ((xo[2] == xo[4]) and (xo[2] ==xo[6])):
        print(xo[2],"WIN")
    elif((xo[3] == xo[4] )and (xo[3] == xo[5])):
        print(xo[3],"WIN")
    elif((xo[4] == xo[1] )and (xo[4] == xo[7])):
        print(xo[4],"WIN")
    elif((xo[6] == xo[7] )and (xo[6] == xo[7])):
        print(xo[6],"WIN")
    else:
        print("DRAW")
main()
