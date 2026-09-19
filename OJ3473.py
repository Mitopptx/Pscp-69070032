"""arrow"""
def main():
    """:3"""
    arrow = input()
    for i in range(1,6):
        count=0
        for j in arrow:
            count +=1
            if i in (1, 5):
                print("  *  ",end="")
            if i in (2,4):
                if (j == "U" and i== 2)or(j=="D" and i == 4):
                    print(" *** ",end="")
                elif (j == "D" and i==2 )or (j=="U"and i==4):
                    print("  *  ",end="") 
                elif j =="L":
                    print(" *   ",end="")
                elif j=="R":
                    print("   * ",end="")
            if i == 3:
                if j in ("U","D"):
                    print("* * *",end="")
                elif j in ("L","R"):
                    print("*****",end="")
            if count!=len(arrow):
                print(end=" ")
        print()
main()
