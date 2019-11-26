from multiprocessing.pool import ThreadPool
from collections import Counter
from itertools import chain

def get_userset(*args):
    monthly_users = set.intersection(*[set(month) for month in args])
    return monthly_users
  
def get_usercounts(*args):
    cnt = Counter(chain(*args))
    return cnt

def id_best_users(*args):

    pool = ThreadPool(processes=2)

    monthly_users_result = pool.apply_async(get_userset, args)
    cnt_result = pool.apply_async(get_usercounts, args)
    
    monthly_users = monthly_users_result.get()
    cnt = cnt_result.get()
    sum = {}

    for k, v in cnt.items():
        if k in monthly_users:
            sum.setdefault(v, []).append(k)
    
    return [[k, sorted(v)] for k, v in sorted(sum.items(), reverse=True)]