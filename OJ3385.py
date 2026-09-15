"""bus"""
def main():
    """:3"""
    capacity = int(input())
    n = int(input())
    stops = [[] for _ in range(n + 1)]
    for _ in range(n):
        data = list(map(int, input().split()))
        stop = data[0]
        stops[stop] = data[1:]
    bus = []
    answer = 0
    for stop in range(1, n + 1):
        bus = [j for j in bus if j != stop]
        for j in stops[stop]:
            if len(bus) < capacity and j > stop:
                bus.append(j)
                answer += 1
    print(answer)
main()
