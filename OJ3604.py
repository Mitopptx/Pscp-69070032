"""tax"""
def main():
    """:3"""
    n = int(input())
    if n<=150000:
        total =0
    elif n <= 300000:
        total = (n-150000)*0.05
    elif n <= 500000:
        total = 7500+((n-300000)*0.1)
    elif n <= 750000:
        total = 27500+((n-500000)*0.15)
    elif n <= 1000000:
        total = 65000+((n-750000)*0.2)
    elif n <= 2000000:
        total = 115000+((n-1000000)*0.25)
    elif n <= 4000000:
        total = 365000+((n-2000000)*0.3)
    else:
        total = 965000+((n-4000000)*0.35)
    print(int(total))
main()
