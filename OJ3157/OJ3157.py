"""all member"""
time = int(input())
score = 0
for time in range(time):
    ch = input()
    if ch == "+":
        score += 10
    elif ch == "-":
        score -= 5
print(score)
