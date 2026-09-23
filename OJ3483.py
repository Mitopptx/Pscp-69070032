"""TEAM UP"""
def main():
    """:3"""
    n,m = map(int,input().split())
    if not 1 <= n <= 10 or not 1 <= m <= 20:
        print("Data Incorrect")
        return
    stat = [0]*m
    total = 0
    for i in range(1,n+1):
        stat = list(map(int,input().split()))
        print(f"Team {i}: Average = {(sum(stat)/m):.2f}, Max = {max(stat)}")
        total += sum(stat)
    print("Total Score of All Teams =",total)
main()
