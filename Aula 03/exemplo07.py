try:
    try:
        x = eval(input("Entre com um número: "))
        print(x)
    finally:
        print("Fazendo x igual ao valor default None")
        x = None
except:
    print("Ocorreu um Erro!")
    print(x)