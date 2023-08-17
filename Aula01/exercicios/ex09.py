# fazer

from array import array
n = int(input("Digite o número de pessoas:"))

i = 0
nomes = []
alturas = array('d')

mais_alto = 0
mais_baixo = 0  

while i < n:
    nome = input("Nome:")
    altura = float(input("Altura:"))
        
    nomes.append(nome)
    alturas.append(altura)
    if alturas[i] <= alturas[mais_baixo]:
        mais_baixo = i
    
    if alturas[i] > alturas[mais_alto]:
        mais_alto = i
    
    i = i + 1
    
    
print(f'A pessoa mais alta é {nomes[mais_alto]} com {alturas[mais_alto]} metros de altura')
print(f'A pessoa mais baixa é {nomes[mais_baixo]} com {alturas[mais_baixo]} metros de altura')