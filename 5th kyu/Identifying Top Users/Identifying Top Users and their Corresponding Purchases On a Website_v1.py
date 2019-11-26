# https://www.codewars.com/kata/5838b5eb1adeb6b7220000f5
from collections import Counter, defaultdict

def id_best_users(*args):

    s = set(args[0])
    for a in args:
        s &= set(a)

    result = Counter()

    for a in args:
        for user in a:
            if user in s:
                result[user] += 1
        
    c = defaultdict(list)
    for k, v in result.items():
        c[v].append(k)

    return sorted([[k, sorted(v)] for (k, v) in c.items()], key=lambda num: num[0], reverse=True)
