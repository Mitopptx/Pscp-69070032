"""fram"""
def main():
    """kasix"""
    s =[0]*5
    s[0] = input()
    s[1] = input()
    s[2] = input()
    s[3] = input()
    s[4] = input()
    size = max(len(s[0]),len(s[1]),len(s[2]),len(s[3]),len(s[4]))
    print("*"*(size+4))
    for i in range(5):
        print("*",s[i],end="")
        print(" "*(size-len(s[i])),"*")
    print("*"*(size+4))
main()
