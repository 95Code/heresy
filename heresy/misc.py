# --- IMPORTS ---

import numpy as np
import time


# --- FUNCTIONS ---

def index(m, n, axis="x"):
    def vector(n):
        n = fix(n)
        x = np.arange(-(n-1)//2, (n+1)//2)
        return x
    
    if m % 2 == 0 or n % 2 == 0:
        print(f"Error! {m} or {n} is not odd!")
        return
    
    M = np.empty((m,n), dtype=np.int32)

    if axis == "x":
        v = vector(n) 
        for k in range(m):
            M[k,:] = v 
    else:
        v = vector(m)
        for k in range(n):
            M[:,k] = v
    
    return M

class Timer(object):
    def __init__(self, name=None):
        self.name = name
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        end = time.time()
        if self.name:
            print(f"[{self.name}]")
        print(f"Elapsed: {end - self.start:.3f}s")


# --- SCRIPT ---

if __name__ == "__main__":
    pass

