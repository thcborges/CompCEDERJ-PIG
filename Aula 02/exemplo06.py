class vetor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, v):
        return vetor(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return vetor(self.x - v.x, self.y - v.y)

    def __repr__(self):
        return "vetor(" + str(self.x) + "," + str(self.y) + ")"


a = vetor(1, 2)
print("a = vetor(1, 2) =", a)

a += vetor(3, 5)
print("a += vetor(3, 5) =",a)

print("a - vetor(2, 2) =", a - vetor(2, 2))

print("a =", a)
