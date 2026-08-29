"""spiderman far from code"""
def main():
    """spiderman brand new code"""
    n= int(input())
    ticket =n
    while ticket>0:
        age,need= map(int,input().split())
        if age<15:
            print("-1")
        elif age<=22 and ticket-need >=0:
            ticket -= need
            print(((need*150)-int((need*150)*20/100)),ticket)
        elif age>=60 and ticket-need >=0:
            ticket -= need
            print(((need*150)-int((need*150)*50/100)),ticket)
        elif ticket-need >=0:
            ticket -= need
            print(need*150,ticket)
        else:
            print("-2")
main()
