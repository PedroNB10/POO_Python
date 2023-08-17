

quant = int(input("Quantos nomes ?:"))

nomes = []

for i in range(quant):
    nome = input ("nome:")

    if nome not in nomes:
        nomes.append(nome)
    else:
        print("o nome ja está na lista !!")


print("\nNomes adicionados\n")
for nome in nomes:
    print(nome)

