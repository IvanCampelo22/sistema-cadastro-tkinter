from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroConteiner = Frame(master)
        self.primeiroConteiner["pady"] = "10"
        self.primeiroConteiner.pack()

        self.titulo = Label(self.primeiroConteiner, text="Sistema de Cadastro", font=self.fontePadrao)
        self.titulo.pack(side=TOP)

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = "5"
        self.segundoContainer.pack()

        self.nome = Label(self.segundoContainer, text="Login: ", font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = "10"
        self.terceiroContainer.pack()

        self.nome = Entry(self.terceiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = "10"
        self.quartoContainer.pack()

        self.senha = Label(self.quartoContainer, text="Senha: ", font=self.fontePadrao)
        self.senha.pack(side=LEFT)

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = "10"
        self.quintoContainer.pack()

        self.verificar = Entry(self.quintoContainer)
        self.verificar["width"] = 30
        self.verificar["font"] = self.fontePadrao
        self.verificar["show"] = "*"
        self.verificar.pack(side=LEFT)

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = "10"
        self.sextoContainer.pack()

        self.autenticar = Button(self.sextoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.autenticar_senha
        self.autenticar.pack()

        self.mensagem = Label(self.primeiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def autenticar_senha(self):
        usuario = self.nome.get()
        senha = self.verificar.get()
        if usuario == "ivan22" and senha == "A1b2c3d4.":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Tente Novamente"


root = Tk()
Application(root)
root.mainloop()
