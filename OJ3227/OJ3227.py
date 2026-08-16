"""ROYAL GAY FLUSH"""
card = input()
if card[0]=="1":
    value = card[0:2]
    symbol = card[2].upper()
else:
    value = card[0].upper()
    symbol = card[1].upper()
if value == "A":
    value = "ace"
elif value =="J":
    value = "jack"
elif value =="Q":
    value = "queen"
elif value =="K":
    value = "king"
if symbol == "D":
    symbol ="diamonds"
elif symbol == "H":
    symbol = "hearts"
elif symbol == "S":
    symbol = "spades"
elif symbol == "C":
    symbol = "clubs"
print(value,"of",symbol)
