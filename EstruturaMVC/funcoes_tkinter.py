import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog



resposta = messagebox.askyesno('Titulo', 'Pergunta?') # nesse caso retorna True ou False

string = simpledialog.askstring('Titulo', 'Digite a string a ser procurada:') # nesse caso retorna a string digitada

messagebox.showinfo('Titulo', 'Mensagem') # nesse caso abre uma janela com a mensagem

messagebox.showerror('Titulo', 'Mensagem') # nesse caso abre uma janela com a mensagem do tipo erro


