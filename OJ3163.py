"""stocking"""
num = int(input())
even =0
odd = 0
sum =0
for i in range(num):
    number = int(input())
    if not number %2:
        even +=1
    else:
        odd +=1
    sum += number
print("SUM",sum)
print("EVEN",even)
print("ODD",odd)
