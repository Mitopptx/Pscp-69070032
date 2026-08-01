str = input()
go,to = str.split()
weight = float(input())
if go == "BKK":
    if to == "CNX":
        print(10+weight*30)
    elif to == "PKT":
        print(25+weight*50)
    else:
        print("Error")
elif go == "CNX" and to =="UBP":
    print(15+weight*40)
elif go == "PKT" and to == "CNX":
    print(30+weight*60)
elif go == "UBP":
    if to== "BKK":
        print(20+weight*40)
    elif to =="PKT":
        print(40+weight*70)
    else:
        print("Error")
else:
    print("Error")
