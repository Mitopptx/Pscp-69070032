"""kohi"""
def main():
    """:3"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    total1 = a + ((e-1)*(((100-b)/100)*a))
    total2 = a*e
    if total2 >= d:
        total2 *= 1-(c/100)
    if total1 < total2:
        print("1")
        print(f"{total1:.2f}")
    else:
        print("2")
        print(f"{total2:.2f}")
main()
