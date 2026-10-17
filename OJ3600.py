"""cal"""
def main():
    """:3"""
    cal=0
    table = {1:100,2:120,3:200,4:60}
    while True:
        n=int(input())
        if n == 5:
            break
        cal += table[n]
    print("Bye Bye")
    print("Total Calories:",cal)
main()
