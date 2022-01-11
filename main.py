from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroConteiner = Frame(master)
        self.primeiroConteiner["pady"] = "10"
        self.primeiroConteiner.pack()

        self.titulo = Button(self.primeiroConteiner)
        self.titulo["text"] = "clique aqui"
        self.titulo["font"] = ("Calibri", "8")
        self.titulo["width"] = 12
        self.titulo["command"] = self.print_hy()
        self.titulo.pack(side=TOP)

        self.mensagem = Label(self.primeiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def print_hy(self):



root = Tk()
Application(root)
root.mainloop()
