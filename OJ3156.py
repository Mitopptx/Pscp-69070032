"""SAWADEE POM HATORI HAEJI"""
word = input()
k = int(input())
n= len(word)
for i in range(n):
    if ord(word[i]) + k>122:
        cha = chr( 96 + (k%26) -(122-ord(word[i])) )
    else:
        cha = chr(ord(word[i]) + k)
    print(cha,end='')
