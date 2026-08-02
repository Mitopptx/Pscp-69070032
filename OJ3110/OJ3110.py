"""MAD PONY"""
stri = input()
go,to = stri.split()
weight = float(input())
if go == "BKK":
    if to == "CNX":
        print(f"{10+weight*30:.2f}")
    elif to == "PKT":
        print(f"{25+weight*50:.2f}")
    else:
        print("Error")
elif go == "CNX" and to =="UBP":
    print(f"{15+weight*40:.2f}")
elif go == "PKT" and to == "CNX":
    print(f"{30+weight*60:.2f}")
elif go == "UBP":
    if to== "BKK":
        print(f"{20+weight*40:.2f}")
    elif to =="PKT":
        print(f"{40+weight*70:.2f}")
    else:
        print("Error")
else:
    print("Error")
