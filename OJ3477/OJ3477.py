"""ADO LOVE PAAD THAIAIII"""
def main():
    """:3"""
    ingrediant = ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
                "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
    checkin = ["Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts",
                "Noodle","Chives","Lime","Egg","Oil","Peanuts"]
    taste = ["Sweet","Sour","Salty"]
    checktaste = ["Sweet","Sour","Salty"]
    tempin = False
    temptaste = False
    while True:
        word = input()
        if word == "Cook":
            break
        if word in ingrediant and word in checkin:
            checkin.remove(word)
        elif word not in ingrediant:
            checkin.append(word)
            tempin = True
    while True:
        word = input()
        if word == "End":
            break
        if word in taste and word in checktaste:
            checktaste.remove(word)
        elif word not in taste:
            checktaste.append(word)
            temptaste = True
    if not checkin and not checktaste:
        print("Delicious!")
    elif not checkin and (temptaste or checktaste):
        print("Not Bad...")
    elif tempin:
        print("This is not Pad Thai!!!")
    else:
        print("This is bad!")
main()
