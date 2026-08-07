"""stocking"""
num = int(input())
even =0
odd = 0
su =0
for num in range(num):
    number = int(input())
    if not number %2:
        even +=1
    else:
        odd +=1
    su += number
print("SUM",su)
print("EVEN",even)
print("ODD",odd)
