"""Graph arai wa"""
def main():
    """:3"""
    word = input()
    mem = {}
    memb = {}
    for i in word:
        if i not in mem:
            mem[i] = 1
        else:
            mem[i] += 1
    mem = dict(sorted(mem.items()))
    for k,v in mem.items():
        if k >= "a":
            print(k,": ",end="")
            count = 0
            for i in range(1,v+1):
                if count==5:
                    print("|",end="")
                    count = 0
                print("-",end="")
                count +=1
            print()
        else:
            memb[k] = v
    for k,v in memb.items():
        print(k,": ",end="")
        count = 0
        for i in range(1,v+1):
            if count==5:
                print("|",end="")
                count = 0
            print("-",end="")
            count+=1
        print()
main()
