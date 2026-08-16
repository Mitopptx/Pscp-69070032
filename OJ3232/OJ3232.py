"""choco frog"""
x,y = map(int,input().split())
count=1
dis=x
while x>0:
    if dis >=y:
        print(count)
        break
    count +=1
    x-=2
    dis+=x
if x<=0 and dis<y:
    print("-1")
