price = int(input())
if (price*10/100)<=50 :
    print(f"{price+50+(price+50)*7/100:.2f}")
elif (price*10/100)>1000 :
    print(f"{price+1000+(price+1000)*7/100:.2f}")
else:
    print(f"{price+(price*10/100)+(price+(price*10/100))*7/100:.2f}")