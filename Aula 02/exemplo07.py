class C:
    def __init__(self, x):
        self.setX(x)

    def getX(self):
        return self.__x

    def setX(self, x):
        if x < 0:
            print("Valor menor que 0")
        elif x > 1000:
            print("Valor maior que 1000")
        else:
            self.__x = x


c1 = C(100)
c2 = C(150)
c1.setX(c1.getX()+c2.getX())
print("c1.getX()", c1.getX())
c1.setX(-10)
