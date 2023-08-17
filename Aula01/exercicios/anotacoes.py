
# importação biblioteca para gerar números aleatórios

import random # importanto pacote
print(random.randrange(1,10))

# importação biblioteca para obter a data

# Temos que importar o módulo datetime
from datetime import datetime,timedelta
data_corrente = datetime.now()
# a função now retorna um objeto datetime
print('Hoje é: ' + str(data_corrente))
# Hoje é: 2020-02-07 16:17:18.694511

print('Dia: ' + str(data_corrente.day))
print('Mês: ' + str(data_corrente.month))
print('Ano: ' + str(data_corrente.year))

# Dia: 7
# Mês: 2
# Ano: 2020

from datetime import datetime
nasc = input('Informe data nasc (dd/mm/yyyy): ')
data_nasc = datetime.strptime(nasc, '%d/%m/%Y') # %d = day, %m = month, %Y = year
print ('Nacimento: ' + str(data_nasc))

um_dia = timedelta(days=1) # timedelta() é uma função para pegar a diferença de tempo analisado para realizar cálculos de datas
vespera_nasc = data_nasc - um_dia # fazendo a diferença de um dia sobre determinada data
print('Véspera do nascimento: ' + str(vespera_nasc))

from array import array # importa a classe array que permite criar arrays ou listas de valores com um tipo de dado específico

notas = array('d') # é um array pois armazena somente tipo double
notas.append(9.2)
notas.append(8.4)

print(notas)
print()
print(notas[1])

alunos_e_notas = []

alunos_e_notas.append("Pedro")
alunos_e_notas.append(10.0)
alunos_e_notas.append("Amanda")
alunos_e_notas.append(9.8)

print(alunos_e_notas)
print(f"\nAluno: {alunos_e_notas[0]}, Nota: {alunos_e_notas[1]}")

nomes = ['Pedro', 'Marina', 'Beto']
alunos = nomes[0:2] # Obtém os dois primeiros itens
# Índice inicial e número de itens a recuperar
print(nomes)
print(alunos)


# para pegar o último delemento de uma lista
minha_lista = [1, 2, 3, 4, 5]
ultimo_elemento = minha_lista[-1]

print(ultimo_elemento)  # Isso imprimirá: 5

from array import array # importa a classe array que permite criar arrays ou listas de valores com um tipo de dado específico

notas = array('d') # é um array pois armazena somente tipo double
notas.append(9.2)
notas.append(8.4)

print(notas)
print()
print(notas[1])

alunos_e_notas = []

alunos_e_notas.append("Pedro")
alunos_e_notas.append(10.0)
alunos_e_notas.append("Amanda")
alunos_e_notas.append(9.8)

print(alunos_e_notas)
print(f"\nAluno: {alunos_e_notas[0]}, Nota: {alunos_e_notas[1]}")


pessoa = {'nome': 'Pedro'} # dicionário é criado com uma chave 'nome' que armazena a string 'Pedro'

pessoa['sobrenome'] = 'Souza'  # um novo par chave e valor é adicionado ao dicionário

print(pessoa) # imprime o dicionário
print(pessoa ['nome']) # imprime o valor associado a chave 'nome'
print(pessoa ['sobrenome']) # imprime o valor associado a chave 'sobrenome'

# .strip() essa função tira o espaço inicial da string e o final também

# quando uma variavel tem um valor padrao dentro de um escopo de código nós usamoos ela dentro do parâmetro com um valor setado, assim elá não precisará ser redefinida toda vez que a função for chamada

def get_inicial(str, maiuscula=True): #nesse caso eu posso passar outro parâmetro para maiuscula
    # caso você queira que o comportamento seja diferente do padrão é só adicionar o parâmetro na chamada da função, no caso de maiuscula não é necessário eu chamá-la também
    if maiuscula:
        inicial = str[0:1].upper()
    else:
        inicial = str[0:1]
    return inicial

nome = input('Digite seu nome: ')
inicial_nome = get_inicial(nome)
print('Sua inicial é: ' + inicial_nome)

def get_inicial(str, maiuscula):
    if maiuscula:
        inicial = str[0:1].upper()
    else:
        inicial = str[0:1]
    return inicial
nome = input('Digite seu nome: ')
inicial_nome = get_inicial(maiuscula=True, str=nome) # aqui você pode observar que é possível trocar a ordem dos parâmetros
print('Sua inicial é: ' + inicial_nome)