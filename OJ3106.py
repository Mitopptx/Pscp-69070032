money = int(input())
if 20000 < money or money%100:
    print("ERROR")
else:
    if money >=1000:
        print("1000 = ",money//1000)
        money -= (money//1000) *1000
    if money >= 500:
        print("500 = ",money//500)
        money -= (money//500)*500
    if money >= 100:
        print("100 = ",money//100)
    
