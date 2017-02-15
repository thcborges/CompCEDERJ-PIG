class B(object):
    n=2
    def f(self, x): return B.n*x


class C(B):
    def f(self, x): return B.f(self, x)**2


    def g(self, x): return self.f(x) + 1


b = B()
c = C()

print(b.f(3))
print(c.f(3))
print(c.g(3))

B.n = 5

print(c.f(3))
