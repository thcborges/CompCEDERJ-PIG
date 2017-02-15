class C (object):
    a = 2
    b = 3

    def f(self, x):
        return C.a * x + C.b


exemplo = C()
print(exemplo.f(7))


C.a = 9
print(exemplo.f(7))

