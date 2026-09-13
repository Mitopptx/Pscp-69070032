"""Dumb trash collector"""
def main():
    """o-o"""
    n = int(input())
    for i in range(n):
        plastic,can,glass =map(float,input().split())
        print(f"{plastic+can+glass:.1f}",end="")
        if plastic+can+glass>50:
            print(", Overloaded",end="")
        if plastic >20:
            print(", Check Type Plastic",end="")
        if can >20:
            print(", Check Type Can",end="")
        if glass >20:
                print(", Check Type Glass",end="")
        print("")
main()
