# importar module sys para pegar o tipo da exception
import sys

lista = ['a', 0, 2]

for elemento in lista:
    try:
        print("O elemento é ", elemento)
        r = 1/int(elemento)
        # caso há alguma falha vai direto para except e não executa linhas posteriores dentro do try
    except:
        print("Oops!", sys.exc_info()[0], "ocorreu") # sys.exc_info() devolve a exceção 
        print("Próxima entrada")
        print()
print("O número recíproco de", elemento , "é", r)