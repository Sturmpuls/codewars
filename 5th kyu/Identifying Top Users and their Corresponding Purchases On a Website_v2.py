from collections import Counter
from itertools import chain

def id_best_users(*args):
    monthly_users = set.intersection(*[set(month) for month in args])
    cnt = Counter(chain(*args))
    sum = {}
    
    for k, v in cnt.items():
        if k in monthly_users:
            sum.setdefault(v, []).append(k)
    
    return [[k, sorted(v)] for k, v in sorted(sum.items(), reverse=True)]