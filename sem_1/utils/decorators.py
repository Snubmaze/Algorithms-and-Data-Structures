import time
import tracemalloc

def timer(func):
    def wrapper(*args, **kwargs):
         start = time.time()
         result = func(*args, **kwargs)
         elapsed = time.time() - start
         print(f"[Execution time]: {elapsed:.6f}s")
         return result
    return wrapper


def memory_counter(func):
     def wrapper(*args, **kwargs):
          tracemalloc.start()
          result = func(*args, **kwargs)
          peak = tracemalloc.get_traced_memory()[1]
          tracemalloc.stop()
          print(
               f"[Peak memory]: {peak / 1024**2:.2f}MB"
               )
          return result
     return wrapper
