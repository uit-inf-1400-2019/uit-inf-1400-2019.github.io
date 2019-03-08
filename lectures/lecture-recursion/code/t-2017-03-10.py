#!/usr/bin/env python3

"""
This is the t.py code that we worked on during the lecture 2017-03-10. 
"""

from tracers import functracer2

def nyttig():
    x = 420
    pass

def foo():
    nyttig()

def hei():
    a = 42
    print(a)
    nyttig()
    foo()

b = 400    
#hei()    

@functracer2
def rec1(i):
    if i > 10:
        return
    print(i)
    rec1(i+1)

#print("Calling rec1()")
#rec1(0)    


@functracer2
def rec_list_maker(i, maxval):
    """Returns a list of values between i and maxval"""
    if i > maxval:
        return []
    newlist = [i] + rec_list_maker(i+1, maxval)
    return newlist

print("Calling rec_list_maker()")
rec_list_maker(3, 6)
