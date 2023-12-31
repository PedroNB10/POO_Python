# Importações necessárias
import tkinter as tk
from tkinter import messagebox

# Classe que define o modelo de um Cliente
class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

# Classe que define a View da aplicação
class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()

        # Rótulos para entrada de dados
        self.labelInfo1 = tk.Label(self.frame1, text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Email: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")

        # Campos de entrada de dados
        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")

        # Botão para salvar dados
        self.buttonSubmit = tk.Button(self.janela, text="Salva")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)

        # Botão para limpar os campos de entrada
        self.buttonClear = tk.Button(self.janela, text="Limpa")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        # Botão para mostrar usuários cadastrados
        self.buttonShow = tk.Button(self.janela, text="Mostrar Usuarios")
        self.buttonShow.pack(side="left")
        self.buttonShow.bind("<Button>", controller.mostraHandler)

    # Função para mostrar uma janela de mensagem
    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

# Classe que atua como o Controller da aplicação
class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e de si próprio (controlador)
        self.view = View(self.root, self)

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    # Manipulador de evento para salvar os dados do cliente
    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        cliente = ModelCliente(nomeCli, emailCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    # Manipulador de evento para limpar os campos de entrada
    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))

    # Manipulador de evento para mostrar os clientes cadastrados
    def mostraHandler(self, event):
        mensagem = ""
        for cliente in self.listaClientes:
            mensagem += cliente.nome + " \n"
        self.view.mostraJanela("Clientes cadastrados:", mensagem)

# Verifica se o código está sendo executado como um script principal
if __name__ == '__main__':
    c = Controller()
