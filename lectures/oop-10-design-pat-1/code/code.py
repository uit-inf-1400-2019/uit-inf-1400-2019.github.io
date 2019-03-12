
import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}s".format(func.__name__, time.time() - now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("\ttest1 called")
def test2(a,b):
    print("\ttest2 called")
def test3(a,b):
    print("\ttest3 called")
    time.sleep(1) 

@log_calls
def test4(a,b):
    print("\ttest4 called")
    time.sleep(1) 

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)
test1(1,2,3)
test2(4,b=5)
test3(6,7)


test4(1,2)

print("-------------")
print("Now decorating aFunction")

# PythonDecorators/my_decorator.py
class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        print("   - wrapped: ", f)
        self.f = f

    def __call__(self):
        print("inside my_decorator.__call__(). Now calling decorated function.")
        self.f()

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction(). Now calling the fuction.")

aFunction()

print("---------")
print("functools example")

from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
   
@fun.register(list)
def _(arg, verbose=False):
    if verbose:
       print("Enumerate this:")
    for i, elem in enumerate(arg):
       print(i, elem)
