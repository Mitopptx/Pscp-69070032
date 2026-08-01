a,b,c= map(int,input().split())
price =(a*25)+(b*40)+(c*55)
if min(a,b,c) >=1:
    print(price-int(price/100*10))
else:
    print(price)
