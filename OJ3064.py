y1= int(input())
m1= int(input())
d1= int(input())
y2= int(input())
m2= int(input())
d2= int(input())
if y1==y2 and m1==m2 and abs(d1-d2)<=7:
  print("0")
elif y1<y2:
  print("1")
elif y1==y2:
  if m1<m2:
    print("1")
  elif m1==m2 and d1-d2<0:
    print("1")
else:
  print("2")
