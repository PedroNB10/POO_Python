from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome,matricula,cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria
    
    @abstractmethod
    def calcularSalario(self):
        pass
    

    def calcularImposto(self,salarioBruto):
        if salarioBruto < 1903.98:
            taxa = 0
        elif salarioBruto < 2826.65:
            taxa = 7.5
        elif salarioBruto  < 3751.05:
            taxa = 15
        elif salarioBruto < 4664.68 :
            taxa = 22.5
        else:
            taxa = 27.5
        return (salarioBruto * taxa) / 100

    
class ProfessorDE(Professor):
    def __init__(self, nome,matricula,cargaHoraria,salarioBruto):
        super().__init__(nome,matricula,cargaHoraria)
        self.__salarioBruto = salarioBruto
        
    @property
    def salarioBruto(self):
        return self.__salarioBruto
    
    @salarioBruto.setter
    def salarioBruto(self,salarioBruto):
        self.__salarioBruto = salarioBruto
    

    def calcularSalario(self):
        
        return self.salarioBruto - (self.calcularImposto(self.salarioBruto)) - self.salarioBruto * 0.11
    

    
    
class ProfessorHorista(Professor):
    def __init__(self, nome,matricula,cargaHoraria,salarioHora):
        super().__init__(nome,matricula,cargaHoraria)
        self.__salarioHora = salarioHora
        
    @property # getter
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter # setter
    def salarioHora(self,salarioHora):
        self.__salarioHora = salarioHora
    

    def calcularSalario(self):
        salbruto = self.cargaHoraria * self.salarioHora
        imposto = self.calcularImposto(salbruto)
        return salbruto - imposto
    
    

        
if __name__ == "__main__":
    professorDE = ProfessorDE('João','123',10,2000)
    professorHorista = ProfessorHorista('Maria','456',2,1000)


    
    lista = [professorDE,professorHorista]
    
    for professor in lista:
        print(f"Nome: {professor.nome}\nSalário: {professor.calcularSalario()}")
        print()
        
        
