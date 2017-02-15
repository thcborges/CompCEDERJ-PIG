try:
    a = eval(input("Entre com um número: "))
    b = eval(input("Entre com outro número: "))
    print(a, "/", b, "=", a/b)

except TypeError:
    print("Erro, tipo errado")
except (Exception) as e:
    print("Erro:", e)
    raise
