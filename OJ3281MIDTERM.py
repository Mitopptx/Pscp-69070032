"""ijudge"""
def main():
    """ijudge"""
    judge = input()
    if judge[:39]=="https://ijudge.it.kmitl.ac.th/problems/":
        code = judge[39:]
        if code[0] in "0123" and len(code)==4 and code.isdigit():
            print(code[0],"STAR")
        elif code[0] in "0123" and len(code)==5 and code[4]=="/" and code[:4].isdigit():
            print(code[0],"STAR")
        else:
            print("INVALID")
    else:
        print("INVALID")
main()
