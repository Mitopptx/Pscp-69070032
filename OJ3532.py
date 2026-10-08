"""GCD"""
def main():
    """:3"""
    num1 = int(input())
    num2 = int(input())
    while num2:
        num1,num2 = num2 , num1% num2
    print(num1)
main()
