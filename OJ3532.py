"""GCD"""
def main():
    """:3"""
    num1 = int(input())
    num2 = int(input())
    for i in range(max(num1,num2),0,-1):
        if not num1%i and not num2%i:
            print(i)
            break
main()
