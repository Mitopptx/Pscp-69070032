"""olympaid"""
def main():
    """:3"""
    n = int(input())
    arr = []
    for _ in range(n):
        word = input()
        j=0
        if arr:
            for i in arr:
                if int(word[4])>int(i[4]):
                    arr.insert(j,word)
                elif int(word[4])==int(i[4]):
                    if int(word[6])>int(i[6]):
                        arr.insert(j,word)
                    elif int(word[6])==int(i[6]):
                        if int(word[8])>int(i[8]):
                            arr.insert(j,word)
                        else:
                            arr.append(word)
                    else:
                        continue
                else:
                    continue
        else:
            arr.append(word)
        print(arr)
        j+=1
    j=0
    for i in arr:
        j+=1
        l = (i[4:8].split())
        med = sum(int(l))
        print(j,i,med)
main()
