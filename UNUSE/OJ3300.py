"""I'm tried so hard I got sofa"""
def main():
    """In the end"""
    n = int(input())
    heavy =0
    chill = 0
    for _ in range(n):
        hour = int(input())
        if hour>18:
            heavy +=1
        else:
            chill +=1
    if heavy-chill>=1:
        total = heavy + chill + (heavy-chill-1)
    else:
        total = heavy + chill
    print(total)
main()
