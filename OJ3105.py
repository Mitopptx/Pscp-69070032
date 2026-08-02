kilo = int(input())
if kilo<=1:
    price=35
elif kilo >10:
    price = 80 +((kilo-10)*8)
else:
    price = 35 + (kilo-1)*5
print(price)
