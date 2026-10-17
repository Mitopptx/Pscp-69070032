"""rabbird"""
def main():
    """:3"""
    a = int(input())
    b = int(input())
    for i in range(a,-1,-1):
        if (i*4)+((a-i)*2) == b:
            print(i,a-i)
            return
    print("Impossible")
main()
