"""calender"""
def main():
    """:3"""
    day = int(input())
    month = int(input())
    year = int(input())
    total = 925142 - (day + (month*30)+ (year*360))
    if total>0:
        print(total)
    else:
        print(0)
main()
