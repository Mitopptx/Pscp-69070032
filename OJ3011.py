c1 = input()
c2 = input()

if c1 == "Red" or c2 == "Red":
    if c1 == "Blue" or c2 == "Blue":
        print("Violet")
    elif c1 == "Yellow" or c2 == "Yellow":
        print("Orange")
    elif c1 == "Red" and c2 == "Red":
        print("Red")
    else:
        print("Error")
elif c1 == "Blue" or c2 == "Blue":
    if c1 == "Yellow" or c2 == "Yellow":
        print("Green")
    elif c1 == "Blue" and c2 == "Blue":
        print("Blue")
    else:
        print("Error")
elif c1 == "Yellow" and c2 == "Yellow":
    print("Yellow")
else:
    print("Error")