"""sairahat"""
def main():
    """:3"""
    num = input()
    if num[:4] =="6807" and 0< int(num[4:]) < 329:
        print("Yes")
    else:
        print("No")
main()
