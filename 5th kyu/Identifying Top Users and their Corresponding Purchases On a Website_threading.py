import threading
import queue
from collections import Counter
from itertools import chain

def get_userset(queue, *args):
    monthly_users = set.intersection(*[set(month) for month in args])
    queue.put(monthly_users)
  
def get_usercounts(queue, *args):
    cnt = Counter(chain(*args))
    queue.put(cnt)

def id_best_users(*args):

    q1 = queue.Queue()
    s = threading.Thread(name='Get Userset', target=get_userset, args=(q1, *args))
    s.setDaemon(True)

    q2 = queue.Queue()
    c = threading.Thread(name='Get Usercounts', target=get_usercounts, args=(q2, *args))
    c.setDaemon(True)
    
    s.start()
    c.start()
    s.join()
    c.join()
    
    monthly_users = q1.get()
    cnt = q2.get()
    sum = {}

    for k, v in cnt.items():
        if k in monthly_users:
            sum.setdefault(v, []).append(k)
    
    return [[k, sorted(v)] for k, v in sorted(sum.items(), reverse=True)]