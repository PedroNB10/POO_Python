import tkinter as tk

from tkinter import messagebox
import music as mus
import artist as art
import album as alb
import playlist as play



class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.main_view = MainView(self.root, self)
        self.root.title("App de Música")


        # self.music_controller = mus.MusicController() # this line instantiate the controller
        self.album_controller = alb.AlbumController(self) # this line instantiate the controller
        self.artist_controller = art.ArtistController(self) # this line instantiate the controller
        self.playlist_controller = play.PlaylistController(self) # this line instantiate the controller

        self.music_controller = mus.MusicController(self) # this line instantiate the controller

        self.root.mainloop()

    def insert_artist(self):
        self.artist_controller.create_insert_artist_view()


    def list_artists(self):
        self.artist_controller.create_search_artist_view()

    def insert_music(self):
        self.album_controller.create_insert_track_view()


    def insert_album(self):
        self.album_controller.create_insert_album_view()


    def list_albuns(self):
        self.album_controller.create_search_albuns_view()
  


    def insert_playlist(self):
        self.playlist_controller.create_insert_playlist_view()


    def list_playlists(self):
        self.playlist_controller.create_search_playlist_view()
   

    def destroy_view(self,view):
        view.destroy()


class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.root_height = 300
        self.root_width = 300
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.root_width/2))
        y_cordinate = int((self.screen_height/2) - (self.root_height/2))
        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))

        self.main_controller = controller
        self.menubar = tk.Menu(self.root)

        self.artist_menu = tk.Menu(self.menubar)
        self.playlist_menu = tk.Menu(self.menubar)
        self.album_menu = tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Album", menu=self.album_menu) # this line add a submenu to the menubar
        self.menubar.add_cascade(label="Artista", menu=self.artist_menu) # this line add a submenu to the menubar
        self.menubar.add_cascade(label="Playlist", menu=self.playlist_menu) # this line add a submenu to the menubar
        self.root.config(menu=self.menubar)
        
        self.artist_menu.add_command(label="Cadastrar", command=self.main_controller.insert_artist) # this line add a command to the submenu option
        self.artist_menu.add_command(label="Consultar", command=self.main_controller.list_artists) # this line add a command to the submenu option
        
        
        self.playlist_menu.add_command(label="Cadastrar", command=self.main_controller.insert_playlist) # this line add a command to the submenu option
        self.playlist_menu.add_command(label="Consultar", command=self.main_controller.list_playlists) # this line add a command to the submenu option
        
        self.album_menu.add_command(label="Cadastrar", command=self.main_controller.insert_album) # this line add a command to the submenu option
        self.album_menu.add_command(label="Consultar", command=self.main_controller.list_albuns)
        self.album_menu.add_command(label="Adicionar Música", command=self.main_controller.insert_music) # this line add a command to the submenu option






if __name__ == "__main__":
    controler = MainController()

