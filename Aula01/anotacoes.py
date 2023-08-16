
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