#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# --- IMPORTS ---

import numpy as np
import time


# --- FUNCTIONS ---

def unify(x):
    prefix = [r"",
              r"k", r"M", r"G", r"T", r"P", r"E", r"Z", r"Y",
              r"y", r"z", r"a", r"f", r"p", r"n", r"µ", r"m"]

    y = np.array(x, dtype=np.float64)
    m = np.abs(y).max()

    if m == 0:
        y = float(y) if y.size == 1 else y 
        return y, ""

    #p = int(np.floor(np.log10(m) / 3))
    p = int(np.log10(10 * m) // 3)
    y /= 10 ** (3 * p) 
    y = float(y) if y.size == 1 else y 
    return y, prefix[p]

def ustr(x):
    x, p = unify(x)
    s = f"{x:3.2f}" + p
    return s

def nprint(A, norm="local", precision=3):
    A = np.asarray(A)
    
    if norm == "global": 
        A, P = unify(A)

    def float_formatter(x):
        if norm == "local":
            x, p = unify(x)

        elif norm == "global":
            p = P

        s = f"{x: > {precision + 5}.{precision}f}" + p + ","

        if p == "":
            s += " "
            
        return s

    formatter = {
        "float_kind": float_formatter,

class Timer(object):
    """ """
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

