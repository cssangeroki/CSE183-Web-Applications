# practical example of decorator: runtime
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        print('######################')        
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1}ms')
        print('######################')
        return result
    return wrapper
    
@performance
def long_time():
    for i in range(10000000):
        i*5
long_time()
