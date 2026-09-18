"""garagade"""
def main():
    """Siuuu"""
    one = input().upper()
    two = input().upper()
    new = ""
    j=0
    if len(one)>len(two):
        for i in range(len(one)):
            j=i
            if i > len(two)-1:
                j -= len(two)
            new += two[j]
    else:
        for i in range(len(two)):
            j=i
            if i > len(one)-1:
                j -= len(one)
            new += one[j]
            one = two
    neww =""
    count = 0
    for i in range(len(new)):
        if new[i] in ("L","O","V","E")or one[i] in ("L","O","V","E"):
            neww += "w"
            count += 1
        else:
            neww += "$"
    if count % 2:
        count = 0
        macount = 0
        con = False
        for i in range(len(neww)):
            if neww[i] == "w":
                if con == True:
                    count += 1
                else:
                    count += 1
                    con= True
            else:
                con ==False
                count = 0
            if macount < count:
                macount = count
        print(neww,macount,sep="")
    else:
        for i in range(len(neww)):
            if neww[i] == "w" and i!=len(neww):
                if neww[i+1] == "w":
                    print(neww)
                    break
                else:
                    print(neww,"#",sep="")
                    break
main()
