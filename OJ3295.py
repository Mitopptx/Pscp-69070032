"""electric bill"""
def main():
    """ka fai"""
    n = int(input())
    if n <=10:
        price= n*5
    elif n<=50:
        price= 50+((n-10)*7)
    elif n <= 100:
        price = 330+((n-50)*10)
    elif n <= 200:
        price = 830+((n-100)*12)
    else:
        price =  2030+((n-200)*15)
    total = price * 100 + price * 7 + n * 50
    total = (total + 5) // 10
    print(f"{total // 10}.{total % 10}")
main()
