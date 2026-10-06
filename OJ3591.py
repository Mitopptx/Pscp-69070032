"""olympaid"""
def main():
    """:3"""
    n = int(input())
    arr = []
    for _ in range(n):
        name, gold, silver, bronze = input().split()
        gold = int(gold)
        silver = int(silver)
        bronze = int(bronze)
        arr.append([name, gold, silver, bronze])
    arr.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))
    rank = 1
    mem = 0
    count = 0
    for i in range(n):
        if i > 0:
            if (arr[i][1], arr[i][2], arr[i][3]) != \
            (arr[i-1][1], arr[i-1][2], arr[i-1][3]):
                rank += 1
        if mem+1 == rank:
            rank += count
            count = 0
        else:
            count +=1
        mem = rank
        name, gold, silver, bronze = arr[i]
        total = gold + silver + bronze
        print(rank, name, gold, silver, bronze, total)
main()
