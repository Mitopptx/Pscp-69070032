"""SAWADEE POM HATORI HAEJI"""
word = input()
k = int(input())
n= len(word)
for i in range(n):
    if ord(word[i]) + k>122:
        cha =chr(97 + ((ord(word[i])-97+k) %26) 
    else:
        cha = chr(ord(word[i]) + k)
    print(cha,end='')
