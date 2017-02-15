class Retangulo:
    def __init__(self, tamanho):
        self.set_tamanho(tamanho)

    def set_tamanho(self, tamanho):
        if min(tamanho) < 0:
            print("Erro!")
        else:
            self.__tamx, self.__tamy = tamanho

    def get_tamanho(self):
        return (self.__tamx, self.__tamy)

    tamanho = property(get_tamanho, set_tamanho)


r = Retangulo((20, 30))
print("r.tamanho", r.tamanho)
r.tamanho = (30, 30)
print("r.tamanho", r.tamanho)
r.tamanho = (-1, 0)
