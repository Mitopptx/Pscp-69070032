"""thai"""
def main():
    """thai help me"""
    name = input()
    age = int(input())
    salary = int(input())
    member = input()
    fam = int(input())
    output = ""
    if age >= 18 and (member=="Y" or salary<=30000):
        if salary <=15000 or member=="Y":
            output = "GOLD"
            money = 3000
            if fam >=3:
                money +=500
        elif salary <=30000:
            output = "SILVER"
            money = 1500
            if fam >=3:
                money +=500
        else:
            output = "NOT ELIGIBLE"
    else:
        output = "NOT ELIGIBLE"
    if output == "NOT ELIGIBLE":
        print(name,output)
    else:
        print(name,output,money)
main()
