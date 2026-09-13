"""raBBit"""
def main():
    """o-o"""
    word = input()
    word = word.upper()
    macount=0
    count=0
    temp=0
    index = -1
    for i in range(len(word)):
        if word[i] == "A":
            if word[i-1]=="R":
                count = 1
                temp = 1
            elif word[i-1]=="A":
                count+=1
            else:
                temp =2
                index = i 
                break
        elif word[i] =="B": 
             if word[i+1] in ("I","T"):
                 temp = 1
             else:
                 temp=2
                 index = i
                 break
        if count>macount:
              macount = count
    if not temp:
         print("unknown",len(word))
    elif temp ==1:
         print("yes",macount)
    elif temp ==2:
         print("no",index)
main()
