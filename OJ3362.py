"""garagade"""
def main():
    """Siuuu"""
    one = input().upper()
    two = input().upper()
    if len(one) < len(two):
        one, two = two, one
    while len(two) < len(one):
        two += two[0]
    neww = ""
    count = 0
    for i,_ in enumerate(one):
        if one[i] in "LOVE" or two[i] in "LOVE":
            neww += "w"
            count += 1
        else:
            neww += "$"
    if count % 2:
        current = 0
        maximum = 0
        for i in neww:
            if i == "w":
                current += 1
                maximum = max(maximum, current)
            else:
                current = 0
        print(neww, maximum, sep="")
    elif "ww" in neww:
        print(neww)
    else:
        print(neww, "#", sep="")
main()
