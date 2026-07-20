"""MILK?"""
a =int(input())
b =int(input())
c =int(input())
d =int(input())
if not b or not d:
    print(d//a)
else:
    bt= d//a
    caps = bt
    while  caps>=b:
        time = caps//b
        new = time*c
        bt+=new
        caps = caps%b+new
    print(bt)
