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
    elif int(number[2])-int(number[4])>5:
        answer +="2"
    else:
        answer +="0"