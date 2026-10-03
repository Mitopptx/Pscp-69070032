"""heat"""
def main():
    """:3"""
    n = int(input())
    heat = list(map(float,input().split()))
    noti = 0
    for i in heat:
        if i >= 37:
            noti += 1
    heat.sort()
    if not n %2:
        med = (heat[n//2] + heat[(n//2)-1]) / 2
    else:
        med = heat[(n//2)]
    print(f"SUM={sum(heat):.2f}\nAVG={sum(heat)/n:.2f}\nMEDIAN={med:.2f}")
    print(f"MAX={max(heat):.2f}\nMIN={min(heat):.2f}\nALERT={noti}\nSORTED=",end="")
    for i in heat:
        print(f"{i:.2f}",end = " ")
main()
