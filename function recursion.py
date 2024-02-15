#function recursion
def rev(n):
    if n<=1:
        return n
    else:
        return n+rev(n-1)
print(rev(5))
