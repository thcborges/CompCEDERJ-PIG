class Time(object):
    ## Classe dos times de futebol
    def __init__(self, nome, campeao, divisao1):
        self.nome = nome
        self.campeao = campeao
        self.divisao1 = divisao1


    def descricao(self):
        ff = "E sou %s. Somos %s" % (self.nome, self.campeao)
        print(ff)


    def div(self):
        if self.divisao1:
            print("Somos da Primeira Divisão")
        else:
            print("Estamos na Segunda Divisão")


Fluminense = Time("tricolor", "tetra-campeões", True)
Fluminense.descricao()
Fluminense.div()
