"""Decode hotel.."""
number = input()
answer = ""
if int(number[0])>5:
    answer += "9"
elif int(number[1])>5:
    answer += "10"
elif int(number[2])>5:
    answer += "11"
elif int(number[3])>5:
    answer += "12"
elif int(number[4])>5:
    answer += "14"
else:
    answer += "13"
if int(number[::1]) == int(number[::-1]):
    if int(number[0])+int(number[4])>5:
        answer += "1"
    elif int(number[1])*int(number[3])>5:
        answer +="2"
    else:
        answer +="0"
else:
     if int(number[0]) // int(number[4])>5:
         answer +="1"
     elif int(number[1]) - int(number[4])>5:
         answer +="2"
     else:
         answer += "0"
total1 = 0
total2 = 1
for i in range(5):
    total1 += int(number[i])
    total2 *= int(number[i])
if total1 >25:
    answer+= "1"
elif total2> 55:
    answer += "2"
else:
    answer += "0"
print(answer)
