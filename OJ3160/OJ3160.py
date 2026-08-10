"""specific num"""
start , stop = map(int,input().split())
prime = 0
num = ""
for i in range(start,stop+1):
    for j in range(2,i+1):
        if i==j:
            prime += 1
            num += str(i) + " "
            break
        if not i % j:
            break
if prime>0:
    print(num.strip())
print("Total primes:", prime)
