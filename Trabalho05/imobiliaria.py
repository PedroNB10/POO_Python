from abc import ABC, abstractmethod


class Venda:
    def __init__(self,codigo_imovel,mes_venda,ano_venda,valor_venda):
        self.__codigo_imovel = codigo_imovel
        self.__mes_venda = mes_venda
        self.__ano_venda = ano_venda
        self.__valor_venda = valor_venda
        
    @property
    def getCodImovel(self):
        return self.__codigo_imovel
    
    @property
    def getMesVenda(self):
        return self.__mes_venda
    
    @property
    def getAnoVenda(self):
        return self.__ano_venda
    
    @property
    def getValorVenda(self):
        return self.__valor_venda
    
    

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []
        
    @property
    def getCodigo(self):
        return self.__codigo
    
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getVendas(self):
        return self.__vendas
    

    def adicionaVenda(self,codigo_imovel,mes_venda,ano_venda,valor_venda):
        self.__vendas.append(Venda(codigo_imovel,mes_venda,ano_venda,valor_venda))
        
    @abstractmethod
    def calculaRenda(self, mes, ano):
        pass
        
    @abstractmethod
    def getDados(self):
        pass
    

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario_fixo, numero_carteira):
        super().__init__(codigo,nome)
        self.__salario_fixo = salario_fixo
        self.__numero_carteira = numero_carteira
        
        
    @property
    def getSalarioFixo(self):
        return self.__salario_fixo
    
    @property
    def getNroCartTrabalho(self):
        return self.__numero_carteira
    
    def getDados(self):
        pass
    
    def calculaRenda(self,mes,ano):
        vendas = self.getVendas.copy()
        vendas_do_mes = [venda.getValorVenda * (1/100) for venda in vendas if venda.getMesVenda == mes and venda.getAnoVenda == ano]
        soma = sum(vendas_do_mes)
            
        return soma + self.__salario_fixo
    
    
    
    
class Comissionado(Vendedor):
    def __init__(self,codigo, nome, cpf, percentual_comissao):
        super().__init__(codigo, nome)
        self.__cpf = cpf
        self.__percentual_comissao = percentual_comissao
        
        
    @property
    def getNroCPF(self):
        return self.__cpf
    
    @property
    def getComissao(self):
        return self.__percentual_comissao
    

    def getDados(self):
        pass
    
    def calculaRenda(self, mes, ano):
        vendas = self.getVendas.copy()
  
        vendas_do_mes = [venda.getValorVenda * (self.getComissao/100) for venda in vendas if venda.getMesVenda == mes and venda.getAnoVenda == ano]
        soma = sum(vendas_do_mes)
            
        return soma
            
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        # print (func.getDados())
        print("Renda no mês 3 de 2022: ")
        print(func.calculaRenda(3, 2022))

    