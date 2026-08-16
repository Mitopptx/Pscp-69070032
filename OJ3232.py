"""choco frog"""
x,y = map(int,input().split())
count=0
dis=0
while x>=0:
    if dis >=y:
        print(count)
        break
    else:
        count +=1
        dis+=x
        x -=2
if x<=0 and dis<y:
    print("-1")
