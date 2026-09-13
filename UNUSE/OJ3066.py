"""same same but diffarent"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 and num2 == num3:
    print("all the same")
elif num1 not in (num2,num3) and num2 not in(num1,num3):
    print("all different")
else:
    print("neither")
