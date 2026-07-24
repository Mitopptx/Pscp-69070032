char =chr(input())
num = int(input())
if char=='H' and num == 4567:
  print("safe unlocked")
elif num==4567:
  print("safe locked - change char")
elif char =='H':
  print("safe locked - change digit")
else:
  print("safe locked")
