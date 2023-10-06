from abc import ABC, abstractclassmethod
from datetime import date

class Conta:
    def __init__(self,nroConta,nome,limite,senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []
        
    @property
    def getNroConta(self):
        return self.__nroConta
    
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getLimite(self):
        return self.__limite
    
    @property
    def getSenha(self):
        return self.__senha
    
    @property
    def getTransacoes(self):
        return self.__transacoes
    
    def adicionaDeposito(self,valor,data,nomeDepositante):
        novo_deposito = Deposito(valor,data,nomeDepositante)
        self.__transacoes.append(novo_deposito)
        return True
    
    def adicionaSaque(self,valor,data,senha):
        
        if senha == self.getSenha and  (self.calculaSaldo() + self.__limite) - valor >= 0:
            novo_saque = Saque(valor,data,senha)
            self.__transacoes.append(novo_saque)
            return True
        
        return False
    
    def adicionaTransf(self,valor,data,senha, contaFavorecido = None):
        if  senha == self.getSenha and (self.calculaSaldo() + self.getLimite) - valor >= 0:
            
            transf_conta_debito = Transferencia(valor,data,senha,"D")
            self.getTransacoes.append(transf_conta_debito)
            

            transf_conta_credito = Transferencia(valor,data,senha,"C")
            contaFavorecido.adicionaTransf(valor, data, senha, None)
            contaFavorecido.getTransacoes.append(transf_conta_credito)
    
            return True
        else:
            return False

            
    def calculaSaldo(self):
        
        lista_valores = []
        for transacao in self.getTransacoes:
            if type(transacao) is Deposito:
                lista_valores.append(transacao.getValor)
            elif type(transacao) is Saque:
                lista_valores.append(transacao.getValor * (-1))
            else:
                if transacao.getTipoTransf == "C":
                    lista_valores.append(transacao.getValor)
                    
                else:
                    lista_valores.append(transacao.getValor * (-1))
                
        return sum(lista_valores) + self.getLimite

    
    
class Transacao(ABC):
    def __init__(self,valor,data):
        self.__valor = valor
        self.__data = data
        
    
    @property
    def getValor(self):
        return self.__valor
    
    @property
    def getData(self):
        return self.__data
    
    
class Saque(Transacao):
    def __init__(self,valor,data,senha):
        super().__init__(valor,data)
        
        self.__senha = senha
    
    @property
    def getSenha(self):
        return self.__senha
    

class Deposito(Transacao):
    def __init__(self,valor,data,nomeDepositante):
        super().__init__(valor,data)    
        self.__nomeDepositante = nomeDepositante
        
    @property
    def getNomeDepositante(self):
        return self.__nomeDepositante
    
    
class Transferencia(Transacao):
    def __init__(self, valor, data,senha,TipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__TipoTransf = TipoTransf
        
        
    @property
    def getSenha(self):
        return self.__senha
    
    @property
    def getTipoTransf(self):
        return self.__TipoTransf

        
        
    
    
    
    
    
    
if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')
        
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprimir 1700