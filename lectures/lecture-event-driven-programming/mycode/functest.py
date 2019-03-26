class Foo:
   def hei(self, arg):
       print "Dette er hei", arg


def func1(arg):
    print "Dette er func1", arg


f = Foo()

func1(42)
f.hei(42)

#dispatcher.register_handler(USEREVENT+1, func1)

a = func1
b = f.hei

a(42)
b(42)