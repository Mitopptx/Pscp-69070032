"""PM"""
def main():
    """PJaaaaa"""
    n = int(input())
    over = 0
    streak = 0
    peak = 0
    start = 0
    best_streak = 0
    best_start = 0
    temp = 0
    for n in range(n):
        num = int(input())
        if num > 50:
            over += 1
            if temp == 1:
                streak += 1
            else:
                streak = 1
                start = n + 1
            temp = 1
            if streak >= best_streak:
                best_streak = streak
                best_start = start
        else:
            temp = 0
            streak = 0
        if peak < num:
            peak = num
    print("OVER = ", over, "\nPEAK = "
        , peak,"\nSTREAK = ", best_streak
        ,"\nSTART = ", best_start, sep="")
main()
