"""elo"""
a = int(input())
b = int(input())
c = input()
Ea=1/(1+(10**((b-a)/400)))
Eb=1/(1+(10**((a-b)/400)))
if c=='A':
    print(f'{Ea:.2f}')
else:
    print(f'{Eb:.2f}')
