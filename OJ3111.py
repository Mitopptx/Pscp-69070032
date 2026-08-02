mem = input()
n = int(input())
price = 0
for _ in range(n):
    price += float(input())
if mem == "Y":
    price -= price*5/100
elif price >=500 and mem=="N":
    price -= price* 3/100
if ((price*1000)%10 >=5):
    price += 0.001
print(round(price,2))
