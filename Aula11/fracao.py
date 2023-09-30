def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

def compararFracoes(f1,f2):
    return (f1.numerador == f2.numerador) and (f1.denominador == f2.denominador)


class Fracao:
    
    def __init__(self,numerador,denominador):
        self.__numerador = numerador
        self.__denominador = denominador
        
    def __str__(self): # sobrescrevendo o método print() para ser possível printar a classe
        return str(self.__numerador) + "/"+ str(self.__denominador)    
    
    def __add__(self,f2): # sobrecarga da função soma
        numerador = self.__numerador * f2.denominador + self.__denominador * f2.numerador
        denominador = self.__denominador * f2.denominador
        divComum = mdc(numerador, denominador)
        
        return Fracao(numerador // divComum, denominador//divComum)
    
    @property
    def numerador(self):
        return self.__numerador
    
    @property
    def denominador(self):
        return self.__denominador
    
    def simplifica(self):
        divComum = mdc(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // divComum
        self.__denominador = self.__denominador // divComum


    
if __name__ == "__main__":
    
    
    frac = Fracao(1,2)
    frac.simplifica()
    frac2 = Fracao(1,2)
    
    print(compararFracoes(frac,frac2))
    print(frac is frac2)
    
    print("Fração 1")
    print(frac)
    print("Fração 2")
    print(frac2)
    print("Soma")
    print(frac + frac2)