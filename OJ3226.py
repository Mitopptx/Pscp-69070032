"""ZIP ZIP ZIP"""
money = float(input())
year = int(input())
for i in range(year):
    money += (money *0.0381*1000//10)/100
print(money)
