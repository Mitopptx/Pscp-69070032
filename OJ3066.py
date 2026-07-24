num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 and num2 == num3:
  print("all the same")
elif num1 != num2 and num2 != num3:
  print("neither")
else:
  print("all different")
