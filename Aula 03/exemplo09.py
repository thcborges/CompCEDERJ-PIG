def gerador():
    for i in range(10):
        print("i = ", i)
        yield i


for j in gerador():
    print("j = ", j)