
def utopian_tree(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n>1:
        if n % 2 == 0:
            return utopian_tree(n-1) + 1
        else:
            return utopian_tree(n-1) *2 
    else:
        return 0
    
