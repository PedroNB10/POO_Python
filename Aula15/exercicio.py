# tk06.py
import tkinter as tk

class GUI:
   def __init__(self):
      self.janela = tk.Tk()
      self.frame1 = tk.Frame(self.janela)
      self.frame2 = tk.Frame(self.janela)
      self.frame1.pack()
      self.frame2.pack()
      
      self.labelInfo1 = tk.Label(self.frame1,text="Digite algo:")
      self.labelResult1 = tk.Label(self.frame2,text="")

      self.labelInfo1.pack(side="left")
      self.labelResult1.pack(side="left")

# aaaaaaaaaaaa

      self.labelInfo2 = tk.Label(self.frame2,text="Digite algo:")
      self.labelResult2 = tk.Label(self.frame2,text="")

      self.labelInfo2.pack(side="left")
      self.labelResult2.pack(side="left")

      
      self.buttonSubmit = tk.Button(self.janela,text="Enter", \
                                    command=self.submit)      
      self.buttonSubmit.pack(side="left")
      
      self.buttonClear = tk.Button(self.janela,text="Clear", \
                                    command=self.clear)      
      self.buttonClear.pack(side="left")
      
      # Criando o objeto Entry
      self.inputText = tk.Entry(self.frame1, width=20)
      self.inputText.pack(side="left")

      self.inputText2 = tk.Entry(self.frame2, width=20)
      self.inputText2.pack(side="left")
      
      self.janela.mainloop()
   
   # Criando as funções de callback
   def submit(self):
      # O texto pode ser recuperado do com o comando get()
      self.labelResult1["text"] = self.inputText.get()
      
   def clear(self):
      self.inputText.delete(0, len(self.inputText.get()))
      self.labelResult1["text"] = ""
   
def main():
   GUI()
   
main()