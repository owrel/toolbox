import time
import functools
import sys
import logging
from typing import TextIO
def memoize(expiry_seconds=-1):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()

            if key in cache and (current_time ==-1 or current_time - cache[key]['timestamp'] < expiry_seconds):
                return cache[key]['result']

            result = func(*args, **kwargs)
            cache[key] = {'result': result, 'timestamp': current_time}
            return result

        return wrapper
    return decorator



def log(stream:TextIO = sys.__stdout__):
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mem = sys.stdout
            logging.root.handlers[0].stream = stream
            sys.stdout = stream
            ret = func(*args, **kwargs)
            sys.stdout = mem
            logging.root.handlers[0].stream = mem
            return ret
        
        return wrapper
    return decorator
