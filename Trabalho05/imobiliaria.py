from abc import ABC, abstractmethod


class Venda:
    def __init__(self,codigo_imovel,mes_venda,ano_venda,valor_venda):
        self.__codigo_imovel = codigo_imovel
        self.__mes_venda = mes_venda
        self.__ano_venda = ano_venda
        self.__valor_venda = valor_venda

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []
        
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def vendas(self):
        return self.__vendas
    

    def adicionarVenda(self,venda):
        self.__vendas.append(venda)
        
    @abstractmethod
    def getDados(self):
        pass
    
    
    
class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario_fixo, numero_carteira):
        super().__init__(codigo,nome)
        self.__salario_fixo = salario_fixo
        self.__numero_carteira = numero_carteira
        
        
    @property
    def salario_fixo(self):
        return self.__salario_fixo
    
    @property
    def numero_carteira(self):
        return self.__numero_carteira
    
    
class Comissionado(Vendedor):
    def __init__(self,codigo, nome, cpf, percentual_comissao):
        super().init(self, codigo, nome)
        self.__cpf = cpf
        self.__percentual_comissao = percentual_comissao
        
        
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def percentual_comissao(self):
        return self.__percentual_comissao
    

    
    
        
        
    
        