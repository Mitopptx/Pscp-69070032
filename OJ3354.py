"""All or notthing"""
def main():
    """f grambler"""
    hint1 = input()
    hint2 = input()
    hint3 = input()
    a = check(hint1)
    b = check(hint2)
    c =check(hint3)
    for i in c:
        for j in b:
            for k in a:
                print(i,j,k,sep="")
def check(word):
    """check"""
    arr =""
    if word[0:2] == "==":
        arr= word[3]
    elif word[0:2] == ">=":
        for i in range(int(word[3]),10):
            arr += str(i)
    elif word[0:2] == "<=":
        for i in range(int(word[3])+1):
            arr += str(i)
    elif word[0:2] == "> ":
        for i in range(int(word[2])+1,10):
            arr += str(i)
    elif word[0:2] == "< ":
        for i in range(int(word[2])):
            arr += str(i)
    elif word[0:2] == "!=":
        for i in range(10):
            if i != int(word[3]):
                arr+= str(i)
    return arr
main()
