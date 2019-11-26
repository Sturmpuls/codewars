# https://www.codewars.com/kata/556deca17c58da83c00002db
def tribonacci(seq, n):

    while len(seq) < n:
    
        next_val = sum(seq[-3:])
        seq.append(next_val)
        
    return seq[:n]
