#!/usr/bin/env python3

"""Function tracer decorators used to track recursive function calls. 
"""

def functracer1(func):
    """Standard decorator function. We can use this to trace function calls (as we saw in oop-07)."""
    def wrapper(*args, **kwargs):
        print("Entering {} with args {} kwargs {}".format(func.__name__, args, kwargs))
        ret = func(*args, **kwargs)
        print("  - returned from {} with return value {}".format(func.__name__, ret))
        return ret
    return wrapper

class functracer2:
    """Similar to functracer1, but this one keeps track of call levels for recursive functions. This can be useful 
    for examining how recursive functions work. """
    def __init__(self, func):
        self.func = func
        self.level = 0
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.level += 1
        indent = "  " * self.level
        print("{}Entering {} with args {} kwargs {}".format(indent, self.func.__name__, args, kwargs))
        ret = self.func(*args, **kwargs)
        print("{}Returning from {} with return value {}".format(indent, self.func.__name__, ret))
        self.level -= 1
        self.ncalls += 1
        if self.level == 0:
            print("{}Total calls: {}".format(indent, self.ncalls))
            self.ncalls = 0
        return ret

