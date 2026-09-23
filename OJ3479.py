"""ROYAL GAY FLUSH"""
def main():
    """:3"""
    card = input()
    if card[0]=="1":
        value = card[0:2]
        symbol = card[2].upper()
    else:
        value = card[0].upper()
        symbol = card[1].upper()
    if value == "A":
        value = "Ace"
    elif value =="J":
        value = "Jack"
    elif value =="Q":
        value = "Queen"
    elif value =="K":
        value = "King"
    if symbol == "D":
        symbol ="Diamonds"
    elif symbol == "H":
        symbol = "Hearts"
    elif symbol == "S":
        symbol = "Spades"
    elif symbol == "C":
        symbol = "Clubs"
    print(value,"of",symbol)
main()
