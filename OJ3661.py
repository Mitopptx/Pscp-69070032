"""kang"""
def main():
    """:3"""
    y = int(input())
    n = int(input())
    current = y
    count=0
    for i in range(n):
        step = int(input())
        if step>y:
            print("NO")
            return
        if current-step>0:
            current-=step
        else:
            current = y
            current-=step
            count+=1
    print(count)
main()
