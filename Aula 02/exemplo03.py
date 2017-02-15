class C(object):
    def __init__(self):
        print("Construtor de C")
        self.x = 1


class D(C):
    def __init__(self):
        print("Construtor de D")
        C.__init__(self)
        self.y = 2


d = D()

print(d.x)
print(d.y)
