class C(object):
    def __init__(self, a, b):
        self.a, self.b = a, b


    def f(self,x):
        return self.a * x + self.b


class D(object):
    def __init__(self, legenda):
        self.legenda = legenda


    def escreve(self, valor):
        print(self.legenda, '=', valor)


class E(C, D):
    def __init__(self, legenda, a, b):
        C.__init__(self, a, b)
        D.__init__(self, legenda)


    def escreve(self, x):
        D.escreve(self, self.f(x))


e = E("f", 10, 3)
e.escreve(4)
