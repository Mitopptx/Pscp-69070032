"""Coke"""
a =int(input())
b =int(input())
c =int(input())
d =int(input())
if not b or c>a or not d:
    print(a*d)
elif b==1:
    print((c*(d-1))+a)

else:
    print((int((d-1)/b))*((a*(b-1))+c)+(((d-1)%b)*a)+a)
