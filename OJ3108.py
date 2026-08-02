"""PrePromotion"""
import math
a,b,c= map(int,input().split())
price =(a*25)+(b*40)+(c*55)
if a+b+c >=3:
    print(math.floor(price-(price/100*10)))
else:
    print(price)
