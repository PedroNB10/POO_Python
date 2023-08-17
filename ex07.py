

valor = int(input("Numero:"))
soma = 0
media = 0
cont = 0

lista = []

while valor != 0:
    lista.append(valor)
    soma = soma + valor
    cont = cont + 1
    valor = int(input("Numero:"))

media = soma / cont

print(media)


