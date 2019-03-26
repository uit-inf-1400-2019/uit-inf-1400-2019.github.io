class Foo:
    def __init__(self, var):
        self.var = var

    def __call__(self, parm):
        print("Called as a function, with parm", parm, "and var", self.var)


f = Foo(42)

f(100)
