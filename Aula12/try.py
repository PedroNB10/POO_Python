
try:
    num = int(input("Digite um número: "))
    assert num % 2 == 0
    
except: # caso ocorra a exception não vai executar o else
    print("Não é um número par!")
    
else: # se não aconteceu o exception executa o else
    reciproco = 1/num
    print(reciproco)