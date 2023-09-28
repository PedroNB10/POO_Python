from abc import ABC, abstractmethod

class Artista():
    def __init__(self,nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def albuns(self):
        return self.__albuns
    
    @property
    def musicas(self):
        return self.__musicas
    
    def adicionarAlbum(self,album):
        self.__albuns.append(album)
        
    def adicionarMusica(self,musica):
        self.__musicas.append(musica)
    
class Album():
    def __init__(self,titulo,artista,ano): # artista é o objeto não o nome
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        
        self.__faixas = []
        artista.adicionarAlbum(self) # instância do album

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def faixas(self):
        return self.__faixas
    
    def adicionarFaixa(self,titulo,artista=None):
        
        if artista is None: # se eu não passo o artista se refere ao artista do próprio album
            artista = self.__artista
            
        numFaixa = len(self.__faixas)
        musica = Musica(titulo,artista,self,numFaixa)
        self.__faixas.append(musica)

class Musica:
    def __init__(self,titulo,artista,album,numeroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__numeroFaixa = numeroFaixa
        
        artista.adicionarMusica(self)
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def album(self):
        return self.__album
    
    @property
    def numeroFaixa(self):
        return self.__numeroFaixa
        
class Playlist:
    def __init__(self,nome):
        self.__nome = nome
        self.__musicas = []
        
    @property
    def nome(self):
        return self.__nome
    

    
    @property
    def musicas(self):
        return self.__musicas
    
    def adicionarMusicaPlay(self,musicaAdicionada):
        self.__musicas.append(musicaAdicionada)
        
        
    
 
if __name__ == "__main__":
    lista_albuns = []
    art1 = Artista("Coldplay")
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.adicionarFaixa("Paradise")
    album1.adicionarFaixa("Hurts like Heaven")
    album1.adicionarFaixa("Charlie Brown")
    lista_albuns.append(album1)
    print(art1.nome)
    
    print(album1.titulo) 
    for musica in album1.faixas:
        print(musica.titulo)
        
    
    play1 = Playlist("Minha Playlist 01")
    
    for musica in album1.faixas:
        play1.adicionarMusicaPlay(musica)
    print(f"Playlist: {play1.nome}")    
    
    for musica in play1.musicas:
        print(musica.titulo)
    print()
    
    #criar e exibir uma playlist com todas as musicas do col