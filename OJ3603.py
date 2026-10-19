"""rabbird"""
def main():
    """:3"""
    a = int(input())
    b = int(input())
    four = (b-(2*a))/2
    two = a- four
    if (not a and b) or (b%2) or (not b and a):
        print("Impossible")
        return
    if (four > -1 and two > -1) and (four+two == a and (4*four)+(2*two) == b):
        print(int(four),int(two))
    else:
        print("Impossible")
main()
