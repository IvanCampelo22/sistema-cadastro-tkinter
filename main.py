import tkinter
from tkinter import *


class Application:
    def __init__(self, master=None):
        root.title("Sistema de Cadastro")
        root.geometry("300x300")
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
        self.sextoContainer.pack(side=LEFT)

        self.autenticar = Button(self.sextoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.autenticar_senha
        self.autenticar.pack(side=LEFT)

        self.setimoContainer = Frame(master)
        self.setimoContainer["padx"] = "10"
        self.setimoContainer.pack(side=RIGHT)

        self.cadastro = Button(self.setimoContainer)
        self.cadastro["text"] = "Cadastrar"
        self.cadastro["font"] = self.fontePadrao
        self.cadastro["width"] = 12
        self.cadastro["command"] = self.cadastrar
        self.cadastro.pack(side=RIGHT)

        self.mensagem = Label(self.primeiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def autenticar_senha(self):
        usuario = self.nome.get()
        senha = self.verificar.get()
        if usuario == "ivan22" and senha == "A1b2c3d4.":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Tente Novamente"

    def cadastrar(self):
        nova_janela = tkinter.Toplevel(root)
        nova_janela.title("Cadastro")
        nova_janela.geometry("300x300")
        titulo_cadastro = tkinter.Label(nova_janela, text="Cadastro", font=self.fontePadrao, pady="10")
        titulo_nome_cadastro = tkinter.Label(nova_janela, text="Nome Completo: ")
        inserir_nome_cadastro = tkinter.Entry(nova_janela)
        email_cadastro = tkinter.Label(nova_janela, text="Informe o Email: ")
        inserir_email_cadastro = tkinter.Entry(nova_janela)
        nome_usuario = tkinter.Label(nova_janela, text="Usuário")
        inserir_nome_usuario = tkinter.Entry(nova_janela)
        senha_cadastro = tkinter.Label(nova_janela, text="Senha")
        inserir_senha_cadastro = tkinter.Entry(nova_janela)
        confirmar = Button(nova_janela, text="Confirmar", command=nova_janela.destroy, padx="10")

        titulo_cadastro.pack()
        titulo_nome_cadastro.pack()
        inserir_nome_cadastro.pack()
        email_cadastro.pack()
        inserir_email_cadastro.pack()
        nome_usuario.pack()
        inserir_nome_usuario.pack()
        senha_cadastro.pack()
        inserir_senha_cadastro.pack()
        confirmar.pack()


root = Tk()
Application(root)
root.mainloop()
