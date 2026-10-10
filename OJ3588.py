"""gcd"""
def main():
    """:3"""
    n = int (input())
    num = [0]*n
    for i in range (n):
        number = int(input())
        num[i] = number
    count =0
    for i in range(max(num),1,-1):
        for j in range(n):
            if num[j] % i:
                count = 0
                break
            else:
                count +=1
        if count == n:
             print(i)
             return
    print(1)
main()
