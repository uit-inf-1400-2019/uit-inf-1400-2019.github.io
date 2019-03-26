
def foo():
    v = 900
    def bar(v=v):
        v = 42
    print v
    bar()
    print v


foo()
