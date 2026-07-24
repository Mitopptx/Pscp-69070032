"""input name sur name year"""
def main():
    """print name surname year+543"""
    name = input()
    sur = input()
    year = int(input())
    year += 543
    if year>=1000:
        year = str(year//1000) +","+ str(year%1000)
    print(name," ",sur[0],". was born in ",year,sep='')
main()
