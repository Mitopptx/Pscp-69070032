year = int(input())
if not year%4:
  if not year%100 and year %400>0:
      print("no")
  else:
      print("yes")
else:
  print("no")
