
txt1 = input("First String:")
txt2 = input("Second String:")

if txt1 in txt2: #verifica se uma string está dentro de outra(uma é substring)
    print("{} is substring of {}".format(txt1,txt2))
else:
    print("{} is substring of {}".format(txt2,txt1))


