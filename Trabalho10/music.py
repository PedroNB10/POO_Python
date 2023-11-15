import tkinter as tk
from tkinter import messagebox


class Music:
    def __init__(self, title, album, artist, track_number):
        self.__title = title
        self.__album = album
        self.__artist = artist
        self.__track_number = track_number

    @property
    def number(self):
        return self.__track_number
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, string):
        self.__artist = string



    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, string):
        self.__title = string

    @property
    def track(self):
        return self.__track
    
    @track.setter
    def track(self, string):
        self.__track = string

class MusicController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.__musics_registrated = []
        self.__musics_registrated_names = []

    def get_music_instance_by_name(self, name):
        for music in self.__musics_registrated:
            if music.title == name:
                return music
        return None

    
    def register_music(self, music, album, artist, track_number):
        music = Music(music, album, artist, track_number)
        self.__musics_registrated.append(music)
        self.__musics_registrated_names.append(music.title)
        return music

    def list_musics_by_artist(self, artist):
        musics = []
        for music in self.__musics_registrated:
            if music.artist == artist:
                musics.append(music)
        return musics
    
    def list_all_musics(self):
        return self.__musics_registrated
    
    def list_all_musics_names(self):
        return self.__musics_registrated_names
    
  
    


