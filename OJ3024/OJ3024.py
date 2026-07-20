"""surpri..what?"""
num1 = float(input())
num2 = float(input())
if (num2*3)-3 < num1:
    print("Not surprising")
elif num1 < 3:
    print("Not surprising")
elif num1 == 3 and num2 == 2:
    print("Not surprising")
else:
    print("Surprising")
