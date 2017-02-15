while True:
    try:
        a = eval(input("Entre com um número: "))
        b = eval(input("Entre com outro número: "))
        print(a, "/", b, "=", a / b)

    except Exception as e:
        print("Erro:", e)
        print("Tente de novo!")
    else:
        break
