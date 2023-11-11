import tkinter as tk
from tkinter import messagebox


class Music:
    def __init__(self, title, album, artist, track_number):
        self.__title = title
        self.__album = album
        self.__artist = artist
        self.__track_number = track_number

    
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


