class Curso:
    def __init__(self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome
    @property
    def getSigla(self):
        return self.__sigla
    
    @property
    def getNome(self):
        return self.__nome
