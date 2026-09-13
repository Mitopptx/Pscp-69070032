"""anotherthai"""
def main():
    """thainot plus"""
    money = int(input())
    days = int(input())
    month = 1000
    success = 0
    statepay = 0
    for _ in range(days):
        items = int(input())
        day = 200
        for _ in range(items):
            price = int(input())
            people_pay = price * 40 // 100
            government = price - people_pay
            if government > day:
                government = day
            if government > month:
                government = month
            pay = price - government
            if money >= pay:
                money -= pay
                day -= government
                month -= government
                statepay += government
                success += 1
    print(success,money,statepay,sep="\n")
main()
