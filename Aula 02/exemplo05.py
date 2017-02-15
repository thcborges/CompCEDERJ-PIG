class C(object):
    def __init__(self, x): self.__x = x

    def incr(self):
        self.__x += 1
        return self.__x


a = C(5)
print("a.incr()", a.incr())
print(a.__x)  ## Gera erro!!! Pois '__' torna um atributo privado do objeto
