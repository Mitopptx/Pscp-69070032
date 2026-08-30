"""anotherthai"""
def main():
    """thainot plus"""
    money = int(input())
    days = int(input())
    half = 1000
    buy = 0
    for _ in range(days):
        exceed = 0
        item = int(input())
        for _ in range(item):
            price = int(input())
            people = price * 40 //100
            temp = min((price - people), 200 - exceed)
            temp = min(temp, half)
            pay = price - temp
            if money >= pay:
                money -= pay
                half -= temp
                exceed += temp
                buy +=1
    print(buy, money, 1000 - half, sep="\n")
main()
