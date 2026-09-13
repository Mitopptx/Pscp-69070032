"""miniexam"""
def main():
    """mini"""
    n = int(input())
    Score = list(map(int,input().split()))
    Top = []
    Zero = []
    team = sum(Score)
    for i in range(n):
        if Score[i] == max(Score):
            Top.append(i+1)
        if not Score[i]:
            Zero.append(i+1)
    print(f"TEAM {team}\nTOP {Top[0]} {max(Score)}")
    print(f"ZERO {" ".join(map(str,Zero))}"if Zero else "ZERO NONE")
main()
