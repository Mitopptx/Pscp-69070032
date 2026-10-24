"""kang"""
def main():
    """:3"""
    planet = list(input().split())
    sun = planet.index("Sun")
    if not sun:
        print("Hot:",planet[1])
    elif sun == len(planet)-1:
        print("Hot:",planet[sun-1])
    else:
        print("Hot:",planet[sun-1],planet[sun+1])
    if sun ==len(planet)-sun -1:
        print("Cool:",planet[0],planet[len(planet)-1])
    elif sun > len(planet)-sun:
        print("Cool:",planet[0])
    else:
        print("Cool:",planet[len(planet)-1])
main()
