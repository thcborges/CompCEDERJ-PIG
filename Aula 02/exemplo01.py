class C(object):
    a = 1
    def f(self, x):
        self.a += x


c = C()
c.f(2)
print("c.a", c.a)
print("C.a", C.a)
