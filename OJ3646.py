"""kang"""
def main():
    """:3"""
    day = input()
    age =int(input())
    height = float(input())
    if (day == "Children Day" and (age <14 and height <=140)) or (day == "Senior Day"and age>=60) or (age<14 and height<90):
        print("FREE")
    else:
        print("PAY")
main()
