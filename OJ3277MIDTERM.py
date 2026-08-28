"""anotherthai"""
def main():
    """thainot plus"""
    import math
    money = int(input())
    day = int(input())
    half =1000
    buy = 0
    exceed =0
    for day in range(day):
        item = int(input())
        for item in range(item):
            price = int(input())
            if (math.ceil(price*60/100) >=200 and half>0) and not exceed:
                temp = 200
                half -= temp
                price-= temp
                exceed = temp
            elif half>0 and exceed<200:
                if exceed + math.ceil(price *60/100)>=200:
                    temp = 200-exceed
                    half -= temp
                    price -= temp
                    exceed =200
                else:
                    temp = math.ceil(price *60/100)
                    half -= temp
                    price -= temp
                    exceed += temp
            if money - price >=0:
                money -= price
                buy +=1
            else:
                half +=temp
                exceed -=temp
        if half>0:
            exceed = 0
    print(buy,money,1000-half,sep="\n")
main()
