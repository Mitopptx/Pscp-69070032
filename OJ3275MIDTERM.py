"""pizza"""
import math
def main():
    """orderme freddy"""
    n = int(input())
    k = int(input())
    m = int(input())
    need = k*n
    order = math.ceil(need/m)
    over = (order*m) - need
    print(need,order,over,sep="\n")
main()
