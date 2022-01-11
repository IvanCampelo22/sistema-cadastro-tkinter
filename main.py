from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroConteiner = Frame(master)
        self.primeiroConteiner["pady"] = "30"
        self.primeiroConteiner.pack()

        self.titulo = Label(self.primeiroConteiner, text="Sistema de Cadastro", font=self.fontePadrao)
        self.titulo.pack(side=TOP)

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = "10"
        self.segundoContainer.pack()

        self.nome = Label(self.segundoContainer, text="Nome: ", font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = "10"
        self.terceiroContainer.pack(side=LEFT)

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.mensagem = Label(self.primeiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def print_hy(self):
        self.mensagem["text"] = "Olá"


root = Tk()
Application(root)
root.mainloop()
