"""garagade"""
def main():
    """Siuuu"""
    one = input().upper()
    two = input().upper()
    new=""
    if len(one)>len(two):
        for i in range(0,len(one),len(two)):
            for j in two:
                new+=j
                i+=1
                if i >= len(one):
                    break
        new2 = one
    else:
         for i in range(0,len(two),len(one)):
            for j in one:
                new+=j
                i+=1
                if i >= len(two):
                    break
         new2 = two
    neww = ""
    count=0
    for i in range(len(new)):
        if new[i] in ("L","O","V","E")or new2[i] in ("L","O","V","E"):
            neww += "w"
            count +=1
        else:
            neww += "$"
    if not count %2:
        for i in range(len(neww)):
           if neww[i] == "w" and neww[i+1]=="w":
               print(neww)
               return
        print(neww,"#",sep="")
    else:
       con = False
       count=0
       mac =0
       for i in neww:
           if i == "w":
               if con:
                   count +=1
                   continue
               con = True
               count =1
           else:
                con = False
           if mac < count:
                mac = count
       print(neww,mac,sep="")             
main()
