"""Bus"""
def main():
    """ahhhh"""
    row = int(input())
    col = int(input())
    sit = int(input())
    if not sit // 10:
        sit = "0"+str(sit)
    for i in range(row,0,-1):
        if not i %2 and i!=row:
            print()
        for j in range (col):
            place = (row*j)+i
            if not place //10:
                place = "0"+str(place)
            if place == sit:
                print("XX",end=" ")
            else:
                print(place,end=" ")
        print()
main()
