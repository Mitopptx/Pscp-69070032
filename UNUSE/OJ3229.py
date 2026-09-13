"""MAX AWOLFEEE"""
base = int(input())
bonus = int(input())
day = int(input())
total = base + bonus
if day >3:
    total *= 1.5
print(int(total))
if total >= 1500:
    print("5")
elif total >= 1000:
    print("4")
elif total >= 500:
    print("3")
elif total >=200:
    print("2")
else:
    print("1")
if total >= 1500 and day >=7:
    print("99")
elif (1500> total >= 1000) and bonus >300:
    print("88")
else:
    print("0")
