"""no time"""
def main():
    """to waste"""
    n = int(input())
    a = int(input())
    minute = n*a
    hour = int(minute/60)
    minute -= hour*60
    if hour>0:
        print(hour,"hours",end=" ")
    if minute>0:
        print(minute,"minute")
    if hour<=0 and minute<=0:
        print("No teaching")
main()
