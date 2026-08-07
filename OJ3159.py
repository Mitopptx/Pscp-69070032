"""tukrorial"""
def fac(n):
    """hh"""
    if n == 1:
        return(n)
    return(n*(fac(n-1)))
number = int(input())
print(fac(number))
