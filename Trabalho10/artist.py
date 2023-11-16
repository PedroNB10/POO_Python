import tkinter as tk
from tkinter import messagebox

class Artist:
    def __init__(self, name):
        self.__name = name
        self.__albums = []
        self.__musics = []

    @property
    def name(self):
        return self.__name
    
    @property
    def albums(self):
        return self.__albums
    
    @property
    def musics(self):
        return self.__musics
    
    def add_album(self, album):
        self.__albums.append(album)

    def add_music(self, music):
        self.__musics.append(music)


class SearchArtistView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Buscar Artista")
        self.geometry("300x300")

        self.controller = controller

        self.label_artist_name = tk.Label(self, text="Nome")
        self.label_artist_name.pack()

        
        self.entry_artist_name = tk.Entry(self)
        self.entry_artist_name.pack()

        self.button_submit = tk.Button(self, text="Buscar", command=controller.search_artist_by_name)
        self.button_submit.pack()


        self.destroy_button = tk.Button(self, text="Concluído", command=lambda: self.destroy())
        self.destroy_button.pack()


class InsertArtistView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title("Inserir Artista")
        self.geometry("300x300")
        self.controller = controller

        self.label_artist_name = tk.Label(self, text="Nome")
        self.label_artist_name.pack()

        
        self.entry_artist_name = tk.Entry(self)
        self.entry_artist_name.pack()

        self.button_submit = tk.Button(self, text="Inserir", command= controller.insert_artist)
        self.button_submit.pack()


        self.destroy_button = tk.Button(self, text="Concluído", command=lambda: self.controller.main_controller.destroy_view(self))
        self.destroy_button.pack()





class ArtistController():
    def __init__(self, main_controller):
        self.artist_list = [] # list of instances of the class Artist
        self.artists_names = [] # list of names of the artists
        self.main_controller = main_controller


    def get_artist_name_by_instance(self, artist_instance):
        return artist_instance.name
    
    def get_artist_instance_by_name(self, artist_name):
        for artist in self.artist_list:
            if artist.name == artist_name:
                return artist
        return None

    def get_artists_names(self):
        return self.artists_names

    def create_search_artist_view(self):
        self.search_artist_view = SearchArtistView(self)

    def create_insert_artist_view(self):
        self.insert_artist_view = InsertArtistView(self)


    def insert_artist(self, artist_name = None):

        if artist_name == None:
            artist_name = self.insert_artist_view.entry_artist_name.get()
            

            if artist_name == "":
                messagebox.showerror("Erro", "O nome do artista não pode ser vazio")
                return
            
            if artist_name in self.artists_names:
                messagebox.showerror("Erro", "O artista já existe")
                return
            else:
                new_artist = Artist(artist_name)
                self.artist_list.append(new_artist) # append the instance of the class Artist to the list
                self.artists_names.append(artist_name) # append the name of the artist to the list
                messagebox.showinfo("Sucesso", f"O Artista {artist_name} foi inserido com sucesso")
                self.insert_artist_view.entry_artist_name.delete(0, len(self.insert_artist_view.entry_artist_name.get()))
        
        else: # if artist_name is not None, then it means that the function was called by the insert_album function
            if artist_name in self.artists_names:
                messagebox.showerror("Erro", "O artista já existe")
                return
            else:
                new_artist = Artist(artist_name)
                self.artist_list.append(new_artist)
                self.artists_names.append(artist_name)

    def search_artist_by_name(self):
        artist_name = self.search_artist_view.entry_artist_name.get()
        if artist_name == "":
            messagebox.showerror("Erro", "O nome do artista não pode ser vazio")
            return
        if artist_name in self.artists_names:
            albuns_list = self.main_controller.album_controller.get_albuns_by_artist(artist_name)
            str = ''
            str += 'Artista: ' + artist_name + '\n\n'
            if len(albuns_list) == 0:
                str += "Nenhum album cadastrado"

            albuns_instances = self.main_controller.album_controller.get_album_list_instances()

            for album in albuns_instances:
                artist_instance = self.main_controller.album_controller.get_album_artist_instance(album)
                if artist_instance.name == artist_name:
                    str += "\n\nAlbum: " + album.title + "\n"
                    str += "Ano: " + album.year + "\n"

                    if len(album.list_tracks()) == 0:
                        str += "Nenhuma música cadastrada\n"
                    else:
                        str += "Músicas: \n"
                        for track in album.list_tracks():
                            str += f'|Faixa - {track.number}| '+ track.title + "\n"

            messagebox.showinfo("Artista", str)
        else:
            messagebox.showerror("Erro", "Artista não encontrado")
            return
        
    # essa função nao precisa mas quero testar
    def show_artists_registered(self):
        string = ""
        for artist in self.artist_list:
            string += artist + "\n"
        messagebox.showinfo("Artistas", string)

    

