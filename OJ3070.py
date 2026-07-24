num = {}
num[0] =int(input())
num[1] =int(input())
num[2]=int(input())
odd=0
even=0
for i in range(3):
  if not num[i]%2:
    even +=1
  else:
    odd +=1
print(even,"\n",odd,sep="")
