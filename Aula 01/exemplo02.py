class C(object):
    def init(self, a=2, b=3):
        self.a = a
        self.b = b


    def f(self, x):
        return self.a * x + self.b


obj1 = C()
obj1.init(2, 3)
obj2 = C()
obj2.init(8, 1)
print(obj1.f(7))
print(obj2.f(7))
