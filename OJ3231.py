"""DICE XIANG TIE"""
guess = int(input())
dice = int(input())
if (guess>6 or guess <1) or (dice>6 or dice <1):
    print("Invalid")
elif guess== dice:
    print("Correct!")
else:
    print("Wrong!")
