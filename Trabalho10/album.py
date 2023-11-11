import tkinter as tk
from tkinter import messagebox

import music as mus

class Album:
    def __init__(self, title, artist, year):
        self.__title = title
        self.__artist = artist
        self.__year = year
        self.__tracks = []

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, string):
        self.__title = string


    @property
    def year(self):
        return self.__year

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, string):
        self.__name = string
    
    @property
    def artist(self):
        return self.__artist
    
    @artist.setter
    def artist(self, string):
        self.__artist = string


    def list_tracks(self):
        return self.__tracks
    
    def add_track(self, track):
        self.__tracks.append(track)


class InsertTrackView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Adicionar Música")
        self.geometry("300x300")
        self.controller = controller

        self.label_track_name = tk.Label(self, text="Nome da música")
        self.label_track_name.pack()

        self.entry_track_name = tk.Entry(self)
        self.entry_track_name.pack()

        self.submit_button = tk.Button(self, text="Inserir", command=controller.insert_track)
        self.submit_button.pack()

        self.destroy_button = tk.Button(self, text="Concluído", command=lambda: self.controller.main_controller.destroy_view(self))
        self.destroy_button.pack()


class SearchAlbumsView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Buscar Albuns")
        self.geometry("300x300")
        self.controller = controller

        self.label_album_name = tk.Label(self, text="Nome")
        self.label_album_name.pack()

        self.entry_album_name = tk.Entry(self)
        self.entry_album_name.pack()

        self.submit_button = tk.Button(self, text="Buscar", command=controller.search_album_by_name)
        self.submit_button.pack()



        self.destroy_button = tk.Button(self, text="Concluído", command=lambda: self.controller.main_controller.destroy_view(self))
        self.destroy_button.pack()



class InsertAlbumView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Inserir Album")
        self.geometry("300x300")
        self.controller = controller

        self.label_album_name = tk.Label(self, text="Nome")
        self.label_album_name.pack()

        self.entry_album_name = tk.Entry(self)
        self.entry_album_name.pack()

        self.label_artist_name = tk.Label(self, text="Artista")
        self.label_artist_name.pack()

        self.entry_artist_name = tk.Entry(self)
        self.entry_artist_name.pack()

        self.label_album_year = tk.Label(self, text="Ano")
        self.label_album_year.pack()

        self.entry_album_year = tk.Entry(self)
        self.entry_album_year.pack()

        self.submit_button = tk.Button(self, text="Inserir", command=controller.insert_album)
        self.submit_button.pack()

        self.add_track_button = tk.Button(self, text="Adicionar Música", command=controller.create_insert_track_view)
        self.add_track_button.pack()

        self.destroy_button = tk.Button(self, text="Concluído", command=lambda: self.controller.main_controller.destroy_view(self))
        self.destroy_button.pack()









class AlbumController:
    def __init__(self, mainController):
        # self.__album_view = AlbumView(self)
        # self.__album_list_view = AlbumListView(self)
        self.main_controller = mainController
        self.album_list = [] # list of instances of Album class
        self.album_names = []

    def get_album_list_instances(self):
        return self.album_list

    def create_insert_album_view(self):
        self.__insert_album_view = InsertAlbumView(self)

    def create_search_albuns_view(self):
        self.__search_albuns_view = SearchAlbumsView(self)

    def create_insert_track_view(self):
        self.__insert_track_view = InsertTrackView(self)


    def search_album_by_name(self):
        album_name = self.__search_albuns_view.entry_album_name.get()
        if album_name == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        for album in self.album_list:
            if album.title == album_name:
                str = ''
                str += 'Nome: ' + album.title + '\n'
                for track in album.list_tracks():
                    str += track.title + '\n'
                messagebox.showinfo("Album", str)
                return

        messagebox.showerror("Erro", "Album não encontrado!")
    
    def insert_track(self):
        track_title = self.__insert_track_view.entry_track_name.get()
        if track_title == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        for album in self.album_list:
            for track in album.list_tracks():
                if track.title == track_title:
                    messagebox.showerror("Erro", "Música já cadastrada!")
                    return
        

        last_album_added = self.album_list[-1]


        last_album_added.add_track(mus.Music(track_title, last_album_added.title, last_album_added.artist, len(last_album_added.list_tracks()) + 1))

        messagebox.showinfo("Sucesso", "Música inserida com sucesso!")

    def insert_album(self):
        album_name = self.__insert_album_view.entry_album_name.get()
        album_artist = self.__insert_album_view.entry_artist_name.get()
        album_year = self.__insert_album_view.entry_album_year.get()

        if album_name == "" or album_artist == "" or album_year == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        artist_instance = self.main_controller.artist_controller.get_artist_instance_by_name(album_artist)

        if artist_instance == None:
            self.main_controller.artist_controller.insert_artist(album_artist)
            artist_instance = self.main_controller.artist_controller.get_artist_instance_by_name(album_artist)
            
        artists_names = self.main_controller.artist_controller.get_artists_names()

        if album_name in self.album_names:
            messagebox.showerror("Erro", "Album já cadastrado!")
            return
        

        album = Album(album_name, album_artist, album_year)
        artist_instance.add_album(album_name)
        self.album_list.append(album)
        self.album_names.append(album_name)
        messagebox.showinfo("Sucesso", "Album inserido com sucesso!")

    def get_albuns_by_artist(self, artist_name):
        list_albuns_by_artist = []

        for album in self.album_list:
            if album.artist == artist_name:
                list_albuns_by_artist.append(album)

        return list_albuns_by_artist
    
