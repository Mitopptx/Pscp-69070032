"""kang"""
def main():
    """:3"""
    n = int(input())
    check = 1
    for i in range(n):
        num = input()
        if int(num[:2])>12 and check != 3:
            check = 2
        if int(num[2:4])>12 and check !=2:
            check = 3
    if check == 1:
        print("no clue")
    elif check ==2 :
        print("ddmmyy")
    elif check ==3:
        print("mmddyy")
main()
