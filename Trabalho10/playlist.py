
class Playlist:
    def __init__(self, name):
        self.__name = name
        self.__musics = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, string):
        self.__name = string

    def list_musics(self):
        return self.__musics
    
    def add_music(self, music):
        self.__musics.append(music)


class PlaylistController:
    def __init__(self, mainController):
        self.main_controller = mainController
        self.playlist_list = []


