from abc import ABC, abstractmethod

# Exceções
#Professor:

class cpfDuplicado(Exception):
    pass

class titulacaoInvalida(Exception):
    pass


class idadeProfessorInvalida(Exception):
    pass

#Aluno

class cursoInvalido(Exception):
    pass

class idadeAlunoInvalida(Exception):
    pass


class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
        
    def getNome(self):
        return self.__nome
    
    def getEndereco(self):
        return self.__endereco
    
    def getCpf(self):
        return self.__cpf
    
    def getIdade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass
    

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso
        
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        
        print(f"Nome: {self.getNome()} -  Endereço: {self.getEndereco()} - Idade: {self.getIdade()} - CPF: {self.getCpf()} - Curso: {self.getCurso()}")

        
        
class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
        
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print(f"Nome: {self.getNome()} -  Endereço: {self.getEndereco()} - Idade: {self.getIdade()} - CPF: {self.getCpf()} - Titulação: {self.getTitulacao()}")
        
    
    
if __name__ == "__main__":
    
    lista_alunos = [
        ("João", "Rua 1", 20, "321321321-00", "SIN"),
        ("Maria", "Rua 2", 30, "987654321-00", "ADM"),
        ("José", "Rua 3", 40, "321321321-00", "CCO"),
        ("Ana", "Rua 4", 50, "456456456-00", "SIN"),
        ("Pedro", "Rua 5", 60, "789789789-00", "ADM"),
        ("Paula", "Rua 6", 70, "321321321-00", "CCO")
    ]
    
    lista_professores = [
        ("João", "Rua 1", 20, "123456789-00", "Doutor"),
        ("Maria", "Rua 2", 30, "987654321-00", "Mestre"),
        ("José", "Rua 3", 40, "321321321-00", "Doutor"),
        ("Ana", "Rua 4", 50, "456456456-00", "Mestre"),
        ("Pedro", "Rua 5", 60, "789789789-00", "Doutor"),
        ("Paula", "Rua 6", 70, "321321321-00", "Mestre")
    ]
    
    professores_cadastrados = {}
    alunos_cadastrados = {}
    
    for nome, endereco, idade, cpf, curso in lista_alunos:
        try:
            
            if  idade < 18:
                raise idadeAlunoInvalida
            
            if curso != "SIN" and curso != "CCO":
                raise cursoInvalido
            
            if cpf in alunos_cadastrados: # verifica dentro do dicionario se o cpf ja foi cadastrado
                raise cpfDuplicado
        
            else:
                alunos_cadastrados[cpf] = Aluno(nome, endereco, idade, cpf, curso)
            
            
        except cursoInvalido:
            print("Curso inválido")
        except idadeAlunoInvalida:
            print("Idade inválida")
        except cpfDuplicado:
            print("CPF duplicado")
        
            
    for nome, endereco, idade, cpf, titulacao in lista_professores:
        try:
            
            if idade < 30:
                raise idadeProfessorInvalida
            
            if titulacao != "Doutor":
                raise titulacaoInvalida
            
            if cpf in professores_cadastrados: # verifica dentro do dicionario se o cpf ja foi cadastrado
                raise cpfDuplicado
        
            else:
                professores_cadastrados[cpf] = Professor(nome, endereco, idade, cpf, titulacao)
            
            
        except titulacaoInvalida:
            print("Titulação inválida")
        except idadeProfessorInvalida:
            print("Idade inválida")
        except cpfDuplicado:
            print("CPF duplicado")
            
    print("Alunos cadastrados")
    for aluno in alunos_cadastrados:
        alunos_cadastrados[aluno].printDescricao()
        
    print("Professores cadastrados")
    for professor in professores_cadastrados:
        professores_cadastrados[professor].printDescricao()
