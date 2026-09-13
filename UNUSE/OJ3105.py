"""FAKE TAXI"""
kilo = int(input())
price = 0
if not kilo:
    price=0
elif kilo<=1:
    price=35
elif kilo >10:
    price = kilo*8
else:
    price = 35 + (kilo-1)*5
print(price)
