# fazer
# precisa terminar!!!
from datetime import datetime,timedelta

def tempoEmSegundos(seg,minutos,horas):
    return seg + minutos * 60 + horas * 60 * 60

def tempoFracionado(seg):
    
    horas = int(seg / 3600)
    minutos = int((seg % 3600)/60)
    seg = seg - horas * 3600 - minutos  * 60

    print(f'O evento tem duração de {horas} horas, {minutos} minutos e {seg} segundos')


hora_entrada = int(input("Digite a hora de entrada:"))
minuto_entrada = int(input("Digite o minuto de entrada:"))
segundo_entrada = int(input("Digite o segundo de entrada:"))

hora_saida = int(input("Digite a hora de saida:"))
minuto_saida = int(input("Digite o minuto de saida:"))
segundo_saida = int(input("Digite o segundo de saida:"))