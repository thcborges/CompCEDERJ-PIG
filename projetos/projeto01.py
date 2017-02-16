class Fracao:
    def __init__(self, n, d):
        self.__numerador = int(n)
        self.__denominador = int(d)
        self.valor = n / d

    def get_numerador(self):
        return self.__numerador

    def get_denominador(self):
        return self.__denominador

    def __repr__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

    def __add__(self, other):
        denominador = self.mmc(self.__denominador, other.get_denominador())
        numerador = (self.op(self.__numerador, denominador, self.__denominador) +
                     self.op(other.get_numerador(), denominador, other.get_denominador()))

        return Fracao(numerador, denominador)

    def __sub__(self, other):
        denominador = self.mmc(self.__denominador(), other.get_denominador())
        numerador = (self.op(self.__numerador, denominador, self.__denominador) -
                     self.op(other.get_numerador(), denominador, other.get_denominador()))

        return Fracao(numerador, denominador)

    def __mul__(self, other):
        return Fracao(self.__numerador * other.get_numerador(), self.__denominador * other.get_denominador())

    def __eq__(self, other):
        return self.__numerador == other.__numerador and self.__denominador == other.__denominador

    def __truediv__(self, other):
        return Fracao(self.__numerador * other.get_denominador(), self.__denominador * other.get_numerador())

    def simplificar(self):
        for i in range(2, min(self.__numerador, self.__denominador)):
            if self.__numerador % i == 0 and self.__denominador % i == 0:
                self.__numerador //= i
                self.__denominador //= i

    @staticmethod
    def op(a, b, c):
        return a * b / c

    def mmc(self, a, b):
        return a * b / self.mdc(a, b)

    def mdc(self, a, b):
        if b == 0:
            return a
        else:
            return self.mdc(b, a % b)


def ler_fracao():
    while True:
        try:
            f = input("Entre com uma fração (num/den): ").split("/")
            frac = Fracao(int(f[0]), int(f[1]))
        except Exception as e:
            print("Erro:", e)
        else:
            break
    return frac


def operacao(frac):
    ops = {"+", "-", "*", "/", "=", "n", "s", "0"}
    operador = input("Qual operação com frações desseja fazer?\n"
                     "'+' para soma,\n"
                     "'-' para subtração,\n"
                     "'*' para multiplicação,\n"
                     "'/' para divisão,\n"
                     "'=' para comparar as frações,\n"
                     "'n' para nova fração,\n"
                     "'s' para simplificar\n"
                     "'0' para sair\n")
    if operador in ops:
        if operador == "+":
            frac += ler_fracao()
            return frac
        elif operador == "-":
            frac -= ler_fracao()
            return frac
        elif operador == "*":
            frac *= ler_fracao()
            return frac
        elif operador == "/":
            frac /= ler_fracao()
            return frac
        elif operador == "=":
            frac == ler_fracao()
            return frac
        elif operador == "n":
            frac = ler_fracao()
            return frac
        elif operador == "s":
            frac.simplificar()
            return frac
        elif operador == "0":
            return None
    else:
        print("Operação incorreta!")
        return operacao(frac)

print("||########################################||\n"
      "||  Bem vindo a calculadora de frações!!  ||\n"
      "||########################################||\n")
fracao = ler_fracao()
print(fracao + Fracao(2, 3))
fracao = operacao(fracao)
while fracao is not None:
    print(fracao)
    fracao = operacao(fracao)
