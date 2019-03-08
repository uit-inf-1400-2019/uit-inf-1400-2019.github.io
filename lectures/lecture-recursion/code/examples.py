#!/usr/bin/env python3
"""Code that we used to develop the idea of recursion. 

The key point to remember is that a function is free to call any
function to help solve its problems, including itself.

To understand how this works, you need to understand how a function
call is normally done. We explained that during the lecture, but the
key points are (slightly simplified):
 
a) when we call another function, we push the point we are at currently to
   the stack (as the return address) as well as any parameters we want to 
   send to the called function
b) a function call is simply
   - a jump to the starting point of another function
   - paramaters on the stack appear as local variables in the function
   - local variables in the function are "pushed on the stack" (actually, 
     room is made for them) and used from the stack
   - when the function returns, it pops the values it no longer needs from 
     the stack, then it pops the return address and jump to that. 

We have ignored return values, but they can be handled in a similar
fashion to parameters.
   
Since you create a new set of variables, parameters etc on the stack
when you call a function, it's easy to see that recursive calls can
function without overwriting the variables in the previous calls as
each call builds on top of the others in the stack:

  [ call 2 with local vars etc.]
  [ call 1 with local vars etc.]
  [ call 0 with local vars etc.]

The difference from a loop is that in a loop like this: 
    def foo(): 
        ...
        doesn't call any functions.
        ... 

    for i in range(10):
        foo()

we only need one level in the stack as we repeatedly (every time we
call foo()) build up the variables and then tear them down again every
time we return from the function:

   [call to foo ]

"""

from tracers import functracer2

########
#
# First recursive examples using decorators. We're recursively creating a list of numbers.
# 
# We need at least one termination condition to avoid infinitely calling ourselves.
# In this case, we have two: "if i > maxval" and  "if i == maxval". Both of these
# conditions lead to return statements without calling rec_list_maker further. 
#

@functracer2
def rec_list_maker(i, maxval):
    """Returns a list of values between i and maxval"""
    if i > maxval:
        return []
    if i == maxval:
        return [maxval]
    return [i] + rec_list_maker(i+1, maxval)

def test_rec_list_maker():
    """A couple of calls to rec_list_maker demonstration the function and the tracing"""
    print("Test 1 of rec_list_maker")
    rec_list_maker(3, 5)
    print("Test 2 of rec_list_maker")
    rec_list_maker(3, 10)
    
test_rec_list_maker()


########
#
# Three variations on parsing a simple graph
# 
def rec_graph_parse1(graph, verbose=True):
    "process items at this level in order" 
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
        elif isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse1(item)

def rec_graph_parse2(graph, verbose=True):
    "process values at this level first, then go deeper" 
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
    for item in graph: 
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse2(item)

def rec_graph_parse3(graph, verbose=True):
    "Go deeper first, then process values at this level" 
    for item in graph: 
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse3(item)
    for item in graph:
        if isinstance(item, int):
            print("** val", item)


simple_graph = [1,2,[3,[4,5],[6,[7]],8],9]

def test_rec():
    # We should kahoot this.
    # Try to predict how each function would go through the graph/tree. 
    for fn in [rec_graph_parse1, rec_graph_parse2, rec_graph_parse3]:
        print("--------------------------")
        print("Recursive graph parsing with", fn.__name__)
        fn(simple_graph)
test_rec()



########
#
# Using the tracing decorator. 
# 

@functracer2
def traced_graph_parser(graph, verbose=True):
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
        elif isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            traced_graph_parser(item)

def test_trace_rec():
    print("--------------------------")
    print("Using the traced graph parser")
    traced_graph_parser(simple_graph)

test_trace_rec()


########
#
# Recursive fibonacci using the tracing decorator. 
# 

@functracer2
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def test_fibonacci():
    for i in range(7):
        print("-------------------")
        print("Testing fibonacci", i)
        fibonacci(i)
    
test_fibonacci()
