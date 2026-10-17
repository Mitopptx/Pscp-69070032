"""balling"""
def main():
    """:3"""
    n = float(input())
    count=-1
    while n >=0.01:
        count+=1
        n = (n*3)/5
    print(count)
main()
