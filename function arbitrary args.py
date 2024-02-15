#function arbitrary args
def sample(*a):
    s=0
    
    for i in a:
        s=s+i
    return s
print(sample(9,7,5))
