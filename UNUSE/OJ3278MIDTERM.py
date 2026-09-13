"""meters"""
def main():
    """maters"""
    num = float(input())
    scale1 = input()
    scale2 = input()
    sen = 0
    if scale1 == "NIU":
        sen = num*1920
    elif scale1 == "KUEP":
        sen = num*160
    elif scale1 == "SOK":
        sen = num*80
    elif scale1 == "WA":
        sen = num*20
    elif scale1 == "SEN":
        sen = num
    if scale2 =="SEN":
        print(f"{sen:.4f}")
    elif scale2 == "WA":
        print(f"{sen/20:.4f}")
    elif scale2 == "SOK":
        print(f"{sen/80:.4f}")
    elif scale2 == "KUEP":
        print(f"{sen/160:.4f}")
    elif scale2 == "NIU":
        print(f"{sen/1920:.4f}")
main()
