"""square"""
def main():
    """:3"""
    n = int(input())
    count=0
    for i in range(1,n+1):
        for j in range(2,n+1):
            if not (i/j)**0.5:
                print("break")
                break
            elif j!=n:
                print("cont")
                continue
            else:
                print("+1")
                count += 1 
                
    print(count)
main()
