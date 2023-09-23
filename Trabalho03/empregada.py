from abc import ABC, abstractmethod

class EmpDoestica(ABC):
    def __init__(self,nome,telefone):
        self.__nome = nome
        self.__telefone = telefone
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone
    
    @abstractmethod
    def getSalario(self):
        pass
    

class Mensalista(EmpDoestica):
    
    def __init__(self,nome,telefone,valorMensal):
        super().__init__(nome,telefone)
        self.__valorMensal = valorMensal
        
        
    @property
    def valorMensal(self):
        return self.__valorMensal
    
    
    def getSalario(self):
        return self.__valorMensal

class Horista(EmpDoestica):
    
    def __init__(self, nome,telefone,horasTrabalhadas,valorPorHora):
        super().__init__(nome,telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora
        
        
    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    @horasTrabalhadas.setter
    def setHorasTrabalhadas(self,horasTrabalhadas):
        self.__horasTrabalhadas = horasTrabalhadas
        
    
    @valorPorHora.setter
    def setValorPorHora(self,valorPorHora):
        self.__valorPorHora = valorPorHora
        
    def getSalario(self):
            return self.__horasTrabalhadas * self.__valorPorHora


class Diarista(EmpDoestica):
    def __init__(self,nome,telefone,diasTrabalhados,valorPorDia):
        super().__init__(nome,telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia
        
    
    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    
    @property
    def valorPorDia(self):
        return self.__diasTrabalhados
    
    
    def getSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia
    
        
        
        
        
        
if __name__ == "__main__":
    emp1 = Diarista("Roberta", 123, 20, 65)
    emp2 = Horista("Angela", 456, 160, 12)
    emp3 = Mensalista("Marta", 235, 1200)
    
    lista = [emp1,emp2, emp3]
    
    
    menor_preco = emp1.getSalario()
    telefone = emp1.telefone
    empregada = emp1.nome

    for emp in lista:
        print(f"Nome : {emp.nome} Salario: {emp.getSalario():.2f} R$ ")
        if emp.getSalario() < menor_preco:
            menor_preco = emp.getSalario()
            empregada = emp.nome
            telefone = emp.telefone
            
    
    print()
    print("Melhor opção:")
    print(f"Nome : {empregada}, Telefone: {telefone}, Valor Mensal: {menor_preco}")

        