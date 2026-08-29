"""mix charem sri"""
def main():
    """python not c++"""
    r1,g1,b1 = map(int,input().split())
    r2,g2,b2 = map(int,input().split())
    mixRGB(r1,g1,b1,r2,g2,b2)
def mixColor(c1,c2):
    """mixky mouse"""
    return int((c1+c2)/2)
def mixRGB(r1,g1,b1,r2,g2,b2):
    """mixky minaj"""
    rmix = mixColor(r1,r2)
    gmix = mixColor(g1,g2)
    bmix = mixColor(b1,b2)
    print(rmix,gmix,bmix)
main()
