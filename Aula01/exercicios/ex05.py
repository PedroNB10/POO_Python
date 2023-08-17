

quant = int(input("Quantos nomes ?:"))

nomes = []

i = 0

while i < quant:
    nome = input("Digite o nome:").strip() 
    if nome in nomes:
        print("Digite um nome que não esteja na lista!!!")
        if i > 1:
            i = i - 1
    else:
        nomes.append(nome)
        i = i + 1
    

print("\nNomes adicionados\n")
for nome in nomes:
    print(nome)
    

nome_procurado = input("Digite o nome a ser procurado:").strip()

if nome_procurado in nomes:
    index = nomes.index(nome_procurado)
    print(f'o nome {nome_procurado} está na posição arr[{index}] ')
else:
    print("Nome não encontrado!")
    
