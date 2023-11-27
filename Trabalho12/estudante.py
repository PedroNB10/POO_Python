import curso as c

class Estudante:
    def __init__(self, nroMatric, nome, curso: c.Curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso
        self.__notas = []

    @property
    def getNroMatric(self):
        return self.__nroMatric
    
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getCurso(self):
        return self.__curso
    
    @property
    def getNotas(self):
        return self.__notas
    

if __name__ == "__main__":
    c1 = c.Curso("CCO", "Ciência da Computação")
    c2 = c.Curso("SIN", "Sistemas de Informação")
    c3 = c.Curso("EEL", "Engenharia Elétrica")
    listaCurso = []
    listaCurso.append(c1)
    listaCurso.append(c2)
    listaCurso.append(c3)
    #Inserir mais cursos, se quiser
    listaEstudante = []
    listaEstudante.append(Estudante(1001, "José da Silva", c1))
    listaEstudante.append(Estudante(1002, "João de Souza", c1))
    listaEstudante.append(Estudante(1003, "Rui Santos", c2))
    #Inserir mais 7 alunos, totalizando pelo menos 10 na lista

