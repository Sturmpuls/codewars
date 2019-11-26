def all_permuted(n):
    # A list of permutations where none of the characters is in its
    # original position is called a "derangement"
    
    der = [
        1 if i == 0 else
        0 if i == 1 else
        1 if i == 2 else
        0 for i in range(n+1)
        ]
    
    for i in range(3, n+1):
        der[i] = (i-1) * (der[i-1] + der[i-2])
    
    return der[n]
