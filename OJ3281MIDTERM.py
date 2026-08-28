"""ijudge"""
def main():
    """ijudge"""
    judge = input()
    if judge[:39]=="https://ijudge.it.kmitl.ac.th/problems/":
        if judge[39] in "0,1,2,3" and len(judge[38:44].split("/")[1])==4:
            print(judge[39],"STAR")
        else:
            print("INVALID")
    else:
        print("INVALID")
main()
