try:
    a = eval(input("Entre com um número: "))
    b = eval(input("Entre com outro número: "))
    print(a, "/", b, "=", a/b)

except (ZeroDivisionError, TypeError):
    print("Erro, segundo número não pode ser zero!")