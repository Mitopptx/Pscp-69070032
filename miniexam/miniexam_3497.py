"""aeiou"""
def main():
    """:3"""
    n = int(input())
    count =0
    a = False
    e = False
    i = False
    o = False
    u = False
    for _ in range(n):
        num = input()
        if num in ("A","E","I","O","U"):
            count +=1
        if num == "A":
            a = True
        if num == "E":
            e = True
        if num == "I":
            i = True
        if num == "O":
            o = True
        if num == "U":
            u = True
    print(count)
    if a and e and i and o and u:
        print("YES")
    else:
        print("NO")
main()
