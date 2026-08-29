"""electric bill"""
def main():
    """ka fai"""
    n = int(input())
    ft = n*0.5
    if n <=10:
        price= n*5
    elif n<=50:
        price= 50+((n-10)*7)
    elif n <= 100:
        price = 330+((n-50)*10)
    elif n <= 200:
        price = 830+((n-100)*12)
    elif n>200:
        price =  2030+((n-200)*15)
    vat=price*7/100
    print(f"{(price+vat+ft):.1f}")
main()
