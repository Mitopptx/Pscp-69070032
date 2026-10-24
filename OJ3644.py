"""kang"""
def main():
    """:3"""
    num = input().strip("[]")
    data = list(num.split(", "))
    n = int(input())
    s = int(input())
    total =0
    for i in range(len(data)):
        mem=0
        for j in range(0,n*s,s):
            if len(data)> i+j:
                mem += int(data[i+j])
            else:
                mem += int(data[i+j-len(data)])
        if total<mem:
            total = mem
    print(total)
main()
