
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print('Algo deu errado ao escrever no arquivo')
    
finally: # caso ocorra ou não o exception vai executar o finally
    f.close()