
# rever

# Exemplos de palíndromos

# numeros pares

# anotaram - maratona
# Ana - Ana
# arara

palavra = input("Digite string:")
palavra_sem_espacos = palavra.replace(" ", "")

palin = True

for i in range(0,int(len(palavra_sem_espacos)/2)):
    if palavra_sem_espacos[i] != palavra_sem_espacos[len(palavra_sem_espacos)-i-1]:
        palin = False
        break

if palin:
    print(palavra + ' é um palíndromo')
        
else:
    print(palavra + ' não é um palíndromo')

