"""Bunny score"""
maxscore = 0
person = 0
num = int(input())
for i in range(num):
    score = int(input())
    if score > maxscore:
        maxscore = score
        person = 1
    elif score == maxscore:
        person +=1

if not maxscore  :
    person = 0
i=0
person+=i
print(maxscore)
print(person)
