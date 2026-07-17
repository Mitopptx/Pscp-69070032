"""Square"""
Xa,Ya,Wa,Ha = map(int,input().split())
Xb,Yb,Wb,Hb = map(int,input().split())
left = max(Xa,Xb)
right = min(Xa+Wa,Xb+Wb)
top = min(Ya+Ha,Yb+Hb)
bttm = max(Ya,Yb)

if left>=right or bttm>=top:
    print("no overlapping")
else:
    print((right-left)*(top-bttm))