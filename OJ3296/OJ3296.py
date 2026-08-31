"""mix charem sri"""
def main():
    """python not c++"""
    r1,g1,b1 = map(int,input().split())
    r2,g2,b2 = map(int,input().split())
    mixrgb(r1,r2)
    mixrgb(g1,g2)
    mixrgb(b1,b2)
def mixcolor(c1,c2):
    """mixky mouse"""
    return int((c1+c2)/2)
def mixrgb(c1,c2):
    """mixky minaj"""
    mix = mixcolor(c1,c2)
    print(mix,end=" ")
main()
