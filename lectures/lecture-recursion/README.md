The question leading up to this extra lecture popped up when using the
Fibonacci example with decorators (oop-07) one of the earlier years.

If you are checking out the code from this lecture, please watch the lecture. 

The general plan for the lecture was: 

- Explain heap.
- Explain stack and relation to function calls.
  - local variables on stack (many languages)
  - save state when calling a new function (push cur position)
  - when entering function: push new variables onto stack.

The main building blocks (the bottom up explanation / what is a function call?)
--------------------

The main idea here is to get a rough idea about how a function call
works so we can see why we can call things recursively.

A function call is usually built up using very simple mechanisms. At
the lowest levels, there isn't anything called a function
call. Instead, it's usually implemented using a simple "jump over
there and continue execution from there", and then using the same
"jump" instruction to jump back to the caller when we return from the
called function. The jump is similar to what we do with
if-statements.

To implement the abstraction of a function call, we need the following
(all of this is handled by the compiler or runtime of the language):

- A way to store the current state of the function (how far we have
  reached when executing the function and the local variables we are
  using). This is necessary to let the called function return back
  here so this function can continue.
- Set up the parameters for the function we are calling.
- Jump to the start (first instruction) of the function we are calling.

``` python
1. def bar(val):
2.    a = 42 + val
3.    return a
4. 
5. def foo():
6.    a = 400
7.    b = 42
8.    c = bar(a)
9     print(a, b, c)
```

In the above example, when `foo` wants to call bar (line 8), it needs to 
- Store the current state (a = 400, b = 42, current position is line 8). 
- Set up parameters to the function call (pass a reference to our local value a). 
- Jump to the first instruction of bar (line 2). 

In stack oriented programming languages, all of this information is
pushed onto a stack that is maintained by the runtime system of the
language. The state that we pushed onto the stack is often called a
"call frame" and is organised in a specific way so that the called
function (`bar`) can inspect it and use it.

To return from a function, we need the following: 
- Some place to store the return value (we can push it onto the stack).
- A method to return to the function that called this function (a simple jump to the position stored in the call frame).
- A method of restoring the state of the calling function after jumping back to it (we can restored it from the stack / call frame).


### The important idea from the low level building blocks

We save the current state, call a function, return from the called
function and restore the current state before continuing.

The implication of this is that a function can call any other
function, including itself! This is the main building block of
recursion! 

### Alternative view (if you find this one easier, otherwise: ignore)

Think about a function call as the equivalent of instantiating an
object. The function source code is like the class, and calling the
function is like creating an object with its own state. Similar to
objects that can create new objects of its own class, a function can
call itself creating a new "instance" of a function call.

### Back to the example

In the above example, `foo` could just as well have been written to
call `foo` instead of `bar`. The only problem with this is that the
next call to foo() would call itself again without returning, and we
have what we call an infinite recursion. The only thing that would
stop this program is that we run out of memory and the program would
crash. 

Exercise: can you see why we end up with infinite recursion in the
above example?

We need something called a termination condition. This is usually just
an if test that causes the function to return without making another
recursive call. This is one of the important things to do correctly
with recursive algorithms. 

### Simple recursive example 

We will show some examples later, but a first simple recursive example is the following:

``` python
def print_numbers(n):
    if n > 10:
       return 
    print(n)
    print_numbers(n+1)

print_numbers(6)
```

Here, the termination condition is that we will no longer call
ourselves if n is larger than 10. To make sure this termination
condition will be reached, we also need to make sure that n will
eventually hit 10 (or higher). In this case we call ourselves with a
higher number than we were called with.

Exercise: try to figure out what happens when we run the program before you run it yourself. 


The main building blocks (the slightly more top down approach)
----------------

A slightly more algorithmically (or mathematically) based idea about
recursion is that a function that gets a problem (through parameters)
can solve that problem by splitting it into two or more smaller
problems and solve them separately.  This approach is also called
"divide and conquer".

A silly little example could be to count the number of items in a list (the length): 

``` python
def recursive_length(lst):
    # we need to do this recursively 
    length = 0 # todo
    return length
```

The first approach is to consider that a list has two parts: 

<ol type="a">
<li> The first item in the list.  </li> 
<li> The rest of the list. </li>
</ol>

Figuring out the length of the list is now simpler: we just need to figure out the length of the two parts. 

The length of a) is simple as it's always 1. 

The length of b) is also simple. We have a function (`recursive_length`) that can tell us this, so we just call that function with the rest (b). 



The code then becomes: 

``` python
def recursive_length(lst):
    # we need to do this recursively 
    a = lst[0]
    b = lst[1:]
    length = 1 + recursive_length(b)
    return length
```

The main problem with this is that it will crash at some point because
we have no termination condition and because it doesn't handle empty
lists very well. We can solve both by changing the code to return 0 if it sees an empty list. 

``` python
def recursive_length(lst):
    # we need to do this recursively 
    if lst == []:
       return 0
    a = lst[0]
    b = lst[1:]
    length = 1 + recursive_length(b)
    return length
```

The function also works for lists of length 1 since `a` will contain
the first (and only) item in the list and `lst[1:]` will return an
empty list.

Exercise: write down lists of lengths 0, 1, 2, 3, and 4. Try to work
out how the function will eventually return the correct length of
each list.


Other demonstraction code (see the code subdirectory): 
--------------------------------------------
- Simple graph: [1,2,[3,[4,5],[6,[7]],8],9]
- Use decorators to decorate recursive function. 
- Fibonacci


Example 1:

```python
def rec_graph_parse1(graph, verbose=True):
    # Process items at this level in order
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
        elif isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse1(item)
```

Example 2:

```python
def rec_graph_parse2(graph, verbose=True):
    # Process values at this level first, then go deeper
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
    for item in graph:
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse2(item)
```

Example 3:

```python
def rec_graph_parse3(graph, verbose=True):
    # Go deeper first, then process values at this level
    for item in graph:
        if isinstance(item, list):
            if verbose:
                print("--> digging in", item)
            rec_graph_parse2(item)
    for item in graph:
        if isinstance(item, int):
            print("** val", item)
```

Kahoot time! 

