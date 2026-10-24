"""kang"""
def main():
    """:3"""
    num = input()
    domain = input()
    if domain =="Domestic" and len(num)==9:
        print(num[0],num[1:5],num[5:9])
    elif domain =="Domestic" and len(num)==10:
        print(num[0:2],num[2:6],num[6:10])
    elif domain =="International" and len(num)==9:
        print("+66",num[1:5],num[5:9])
    elif domain =="International" and len(num)==10:
        print("+66",num[1]," ",num[2:6]," ",num[6:10],sep="")
main()
