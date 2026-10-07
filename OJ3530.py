"""square"""
def main():
    """:3"""
    n = int(input())
    count=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if not i%j:
                continue
            elif i == j:
                if not i%(j**2):
                    break
                if j==i or i == 1:
                    count += 1 
                    break
                continue
    print(count)
main()
