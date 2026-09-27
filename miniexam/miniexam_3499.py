"""noodle"""
def main():
    """:3"""
    price = int(input())
    pay = int(input())
    total = pay-price
    if total >0:
        print(total)
    elif not total:
        print("Good!")
    else:
        print("Need more cash!")
main()
