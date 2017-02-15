class Retangulo:
    def __init__(self, tamanho):
        self.setTamanho(tamanho)

    def setTamanho(self, tamanho):
        if min(tamanho) < 0:
            print("Erro!")
        else:
            self.__tamx, self.__tamy = tamanho

    def getTamanho(self):
        return (self.__tamx, self.__tamy)


r = Retangulo((20, 30))
print(r.getTamanho())
r.setTamanho((-1, 0))
