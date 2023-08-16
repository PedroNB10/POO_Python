from datetime import datetime, timedelta
nasc = input('Qual é sua data de nascimento (dd/mm/yyyy): ')
data_nasc = datetime.strptime(nasc, '%d/%m/%Y')
#segunda = 0
#terca = 1
#...

data_nasc = (data_nasc.weekday())

if data_nasc == 0:
    data_nasc = "segunda"
elif data_nasc == 1:
    data_nasc = "terça"
elif data_nasc == 2:
    data_nasc = "quarta"
elif data_nasc == 3:
    data_nasc = "quinta"
print ('Dia da semana que você nasceu: ' + data_nasc)


