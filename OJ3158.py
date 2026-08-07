"""two of idk"""
def two(n):
    """twoooo"""
    if n == 1:
        return(1)
    return(n**2+(two(n-1)))
number = int(input())
print(two(number))
