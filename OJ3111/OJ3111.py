"""SCHOOL OF ASHES"""
mem = input()
n = int(input())
price = 0
for n in range(n):
    price += float(input())
if mem == "Y":
    price -= price* 5/100
elif price >=500 and mem=="N":
    price -= price* 3/100
price += 0.001
print(f"{price:.2f}")
