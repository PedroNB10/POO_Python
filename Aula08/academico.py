from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__lista_disciplinas = []

    @property # getter
    def nome(self):
        return self.__nome
    
    @property # getter
    def endereco(self):
        return self.__endereco
    
    @property # getter
    def idade(self):
        return self.__idade
    
    @property # getter
    def lista_disciplinas(self):
        return self.__lista_disciplinas
    
    @abstractmethod # método abstrato
    def printDescricao(self):
        pass # não faz nada, só serve para indicar que o método é abstrato
    
    def inserir_disciplina(self, disciplina):
        self.__lista_disciplinas.append(disciplina)
    
class Professor(Pessoa):
    def __init__(self, nome, endereco, idade,titulacao):
        super().__init__(nome, endereco, idade) # chama o construtor da classe mãe
        self.__titulacao = titulacao # atributo específico de professor
        
    @property
    def titulacao(self):
        return self.__titulacao 
    
    
    def printDescricao(self): # método abstrato da classe mãe
        print("Nome: ", self.nome)
        print("Endereço: ", self.endereco)
        print("Idade: ", self.idade)
        print("Titulação: ", self.titulacao)
        print("Disciplinas Ministradas: ")
        for disciplina in self.lista_disciplinas:
            print(f"Nome {disciplina.nome} - CH {disciplina.carga_horaria}")

    

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade,curso):
        super().__init__(nome, endereco, idade) # chama o construtor da classe mãe
        self.__curso = curso # atributo específico de aluno
        
    @property
    def curso(self):
        return self.__curso 
    
    
    def printDescricao(self): # método abstrato da classe mãe
        print("Nome: ", self.nome)
        print("Endereço: ", self.endereco)
        print("Idade: ", self.idade)
        print("Curso: ", self.curso)
        print("Disciplinas Cursadas: ")
        for disciplina in self.lista_disciplinas:
            print(f"Nome {disciplina.nome} - CH {disciplina.carga_horaria}")    
            
class Disciplina():
    def __init__(self, nome, carga_horaria):
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
if __name__ == "__main__":
    
    D1 = Disciplina("POO", 60)
    D2 = Disciplina("Banco de dados", 64)
    D3 = Disciplina("Estrutura de dados", 65)
     
    professor = Professor("João", "Rua 1", 30, "Doutorado")
    professor.inserir_disciplina(D1)
    professor.inserir_disciplina(D2)
    aluno = Aluno("Roberto", "Rua 3", 20, "SIN")
    aluno.inserir_disciplina(D1)
    aluno.inserir_disciplina(D3)
    professor.printDescricao()
    aluno.printDescricao()
    
