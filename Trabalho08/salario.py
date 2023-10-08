from abc import ABC, abstractclassmethod




class Funcionario(ABC):
    def __init__(self,codigo,nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = [] # lista de fichas mensais
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    
    def adicionaPonto(self,mes, ano, faltas, atrasos):
        self.__pontoMensalFunc.append(PontoFunc(mes, ano, faltas, atrasos))

    
    def lancaFaltas(self, mes, ano, faltas):
        lista = self.__pontoMensalFunc
        
        for ficha in lista:
            if ficha.mes == mes and ficha.ano == ano:
                ficha.lancaFaltas(ficha.nroFaltas + faltas)
                break
        
    
    def lancaAtrasos(self, mes, ano, faltas):
        lista = self.__pontoMensalFunc
        
        for ficha in lista:
            if ficha.mes == mes and ficha.ano == ano:
                ficha.lancaAtrasos(faltas)
    
    def imprimeFolha(self, mes, ano):
        print("Código:  ",self.__codigo)
        print("Nome: ", self.__nome)
        num_formatado = f"{(self.calculaSalario(mes,ano)):.2f}"
        print("Salário Líquido: ", num_formatado)
        num_formatado = f"{(self.calculaBonus(mes,ano)):.2f}"
        print("Bônus: ",num_formatado )

    
    @abstractclassmethod
    def calculaSalario(self, mes, ano): # precisa retornar o salario
        pass
    
    @abstractclassmethod
    def calculaBonus(self, mes, ano):
        pass
    

class Professor(Funcionario):
    def __init__(self, codigo,nome, titulacao, salarioHora, nroHoras):
        super().__init__(codigo,nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroHoras = nroHoras
        
        
    @property
    def titulacao(self):
        return self.__titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @property
    def nroHoras(self):
        return self.__nroHoras
    
    def calculaSalario(self, mes, ano):
        lista = self.pontoMensalFunc
        total_faltas = 0
        for ponto in lista:
            
            if ponto.mes == mes and ponto.ano == ano:
                total_faltas = ponto.nroFaltas
                break
            
        return self.__salarioHora * self.__nroHoras - self.__salarioHora * total_faltas
                
    def calculaBonus(self, mes, ano):
        lista = self.pontoMensalFunc
        total_atrasos = 0
        for ponto in lista:
            if ponto.mes == mes and ponto.ano == ano:
                total_atrasos = ponto.nroAtrasos
                break
                
        if total_atrasos == 0:
            porcentagem_bonus = 10/100
        elif total_atrasos < 10:
            porcentagem_bonus = (10 - total_atrasos) / 100
        else:
            porcentagem_bonus = 0
            
        salario_liquido = self.calculaSalario(mes,ano)
        return salario_liquido * porcentagem_bonus
    
    
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo,nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal
        
        
    @property
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    def calculaSalario(self, mes, ano):
    
        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                total_faltas = ponto.nroFaltas
                break
            
        return self.__salarioMensal - ((self.__salarioMensal/30) * total_faltas )
                
    def calculaBonus(self, mes, ano):

        for ponto in self.pontoMensalFunc:
            if ponto.mes == mes and ponto.ano == ano:
                total_atrasos = ponto.nroAtrasos
                break
                
        if total_atrasos == 0:
            porcentagem_bonus = 8/100
        elif total_atrasos < 8:
            porcentagem_bonus = (8 - total_atrasos) / 100
        else:
            porcentagem_bonus = 0
            
        salario_liquido = self.calculaSalario(mes,ano)
        return salario_liquido * porcentagem_bonus
        
class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos
        
        
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def nroFaltas(self):
        return self.__nroFaltas


    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(self, nroFaltas):

        self.__nroFaltas += nroFaltas
        
    def lancaAtrasos(self, nroAtrasos):
        self.__nroAtrasos += nroAtrasos
        
        
       
        
       
if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()