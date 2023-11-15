import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class Playlist:
    def __init__(self, name, musics):
        self.__name = name
        self.__musics = musics
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, string):
        self.__name = string

    def list_musics(self):
        return self.__musics
    


class SearchPlaylistView(tk.Toplevel):
    def __init__(self, controller):
        self.controller = controller
        super().__init__()
        self.title("Buscar Playlist")
        self.geometry("300x300")

        self.frame_search = tk.Frame(self)
        self.frame_search.pack()
        self.label_search = tk.Label(self.frame_search, text="Informe o nome da playlist: ")
        self.label_search.pack(side="left")
        self.input_search = tk.Entry(self.frame_search, width=20)
        self.input_search.pack(side="left")
        self.search_button = tk.Button(self, text="Buscar", command=controller.show_tracks_from_playlist)
        self.search_button.pack()
        



class InsertPlaylistView(tk.Toplevel):
    def __init__(self, controller, artists_list, musics_list):
        super().__init__()
        self.title("Inserir Playlist")
        self.geometry("350x450")
        self.controller = controller

        self.frame_name_playlist = tk.Frame(self)
        self.frame_name_playlist.pack()

        self.frame_artist = tk.Frame(self)
        self.frame_artist.pack()

        self.frame_musics = tk.Frame(self)
        self.frame_musics.pack()

        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack()
        

        self.label_playlist_name = tk.Label(self.frame_name_playlist,text="Informe o nome da playlist: ")
        self.label_playlist_name.pack(side="left")

        self.input_name_playlist = tk.Entry(self.frame_name_playlist,width=20)
        self.input_name_playlist.pack(side="left")

        



        self.label_artist_name = tk.Label(self.frame_artist,text="Escolha o artista: ")
        self.label_artist_name.pack(side="left")

        self.select_combo_box = tk.StringVar()
        self.combobox = ttk.Combobox(self.frame_artist, width = 15 , textvariable = self.select_combo_box)
        self.combobox.pack(side="left")
        self.combobox['values'] = artists_list


        
        
        self.label_music_name = tk.Label(self.frame_musics,text="Escolha a musica: ")

        
        self.listbox = tk.Listbox(self.frame_musics)
        self.listbox.pack(side="left")
        for music in musics_list:
            self.listbox.insert(tk.END, music)


        self.combobox.bind("<<ComboboxSelected>>", self.controller.update_listbox)





        self.add_music_button = tk.Button(self.frame_buttons, text="Adicionar Música")
        self.add_music_button.pack(side="left")

        self.add_music_button.bind("<Button>", controller.add_music)


        self.create_playlist_button = tk.Button(self.frame_buttons, text="Criar Playlist")
        self.create_playlist_button.pack()
        self.create_playlist_button.bind("<Button>", controller.create_playlist)









class PlaylistController:
    def __init__(self, mainController):
        self.main_controller = mainController
        self.playlist_list = []
        self.playlist_names = []

    
    def update_listbox(self, event):
        print("update_listbox")
        print("combobox selected: ", self.insert_playlist_view.select_combo_box.get())
        self.insert_playlist_view.listbox.delete(0, tk.END) # clear listbox
        

        selected_artist = self.insert_playlist_view.select_combo_box.get()

        for music in self.main_controller.music_controller.list_all_musics():
            print("music.artist: ", music.artist.name)
            print("selected_artist: ", selected_artist)
            if music.artist.name == selected_artist and music not in self.tracks_added_to_playlist:
                self.insert_playlist_view.listbox.insert(tk.END, music.title)

    def get_playlist_instance_by_name(self, playlist_name):
        for playlist in self.playlist_list:
            if playlist.name == playlist_name:
                return playlist
        return None

    def create_search_playlist_view(self):
        self.search_playlist_view = SearchPlaylistView(self)

    def create_insert_playlist_view(self):
        self.tracks_added_to_playlist = []
        artists_list = self.main_controller.artist_controller.artists_names
        musics_list = self.main_controller.music_controller.list_all_musics_names()
        self.insert_playlist_view = InsertPlaylistView(self, artists_list, musics_list)


    def create_playlist(self, event):
        name = self.insert_playlist_view.input_name_playlist.get()
        if name == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if name in self.playlist_names:
            messagebox.showerror("Erro", "Playlist já existente")
            return
        
        messagebox.showinfo("Sucesso", f"Playlist {name} criada com sucesso")
        new_playlist =  Playlist(name, self.tracks_added_to_playlist)

        self.playlist_list.append(new_playlist)
        self.playlist_names.append(name)
        self.main_controller.destroy_view(self.insert_playlist_view)
    
    def add_music(self, event):

        music_selected = self.insert_playlist_view.listbox.get(tk.ACTIVE)

        if not music_selected: # 
            messagebox.showerror("Erro", "Selecione uma música para adicionar")
            return
               
        music_instance = self.main_controller.music_controller.get_music_instance_by_name(music_selected)
        self.tracks_added_to_playlist.append(music_instance)
        self.insert_playlist_view.listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Sucesso", f"A Música '{music_instance.title}' foi adicionada com sucesso")

    def show_tracks_from_playlist(self):
        playlist_name = self.search_playlist_view.input_search.get()
        playlist_instance = self.get_playlist_instance_by_name(playlist_name)

        if playlist_instance == None:
            messagebox.showerror("Erro", "Playlist não encontrada")
            return
        
        str = ''
        str += 'Nome da Playlist: ' + playlist_instance.name + '\n'
        for music in playlist_instance.list_musics():
            str += f'|Faixa - {music.number}| '+ music.title + "\n"

        messagebox.showinfo("Playlist", str)

        
        

    





        




