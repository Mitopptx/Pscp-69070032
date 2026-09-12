"""diff"""
def main():
    """o-o"""
    txt = input()
    txt = txt.strip("]\r")
    txt = txt.strip("[")
    num = txt.split(", ")
    temp =0
    for i in num:
        if not int(i)%2:
            print(i)
            temp=1
    if not temp:
        print("Nope")
main()
