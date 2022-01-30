from doctest import master
import tkinter
from tkinter import *


import servico_cadastro, Banco
from alunos_cadastro import Alunos
from servico_cadastro import *


class Application:
    def __init__(self, master=None):
        root.title("Escola Municipal")
        root.geometry("300x300")
        self.fontePadrao = ("Arial", "10")
        self.primeiroConteiner = Frame(master)
        self.primeiroConteiner["pady"] = "10"
        self.primeiroConteiner.pack()

        self.titulo = Label(self.primeiroConteiner, text="Entre com seu login e senha", font=self.fontePadrao)
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

        self.txtlogin = Entry(self.terceiroContainer)
        self.txtlogin["width"] = 30
        self.txtlogin["font"] = self.fontePadrao
        self.txtlogin.pack(side=LEFT)

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = "10"
        self.quartoContainer.pack()

        self.txtsenha = Label(self.quartoContainer, text="Senha", font=self.fontePadrao) 
        self.txtsenha.pack(side=LEFT)

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = "10"
        self.quintoContainer.pack()

        self.txtverificar = Entry(self.quintoContainer)
        self.txtverificar["width"] = 30
        self.txtverificar["font"] = self.fontePadrao
        self.txtverificar["show"] = "*"
        self.txtverificar.pack(side=LEFT)

        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = "10"
        self.sextoContainer.pack(side=LEFT)

        self.autenticar = Button(self.sextoContainer)
        self.autenticar["text"] = "Entrar"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.InserirUsuario
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
        
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def autenticar_senha(self):
        usuario = self.nome.get()
        senha = self.verificar.get()
        if usuario == "ivan22" and senha == "A1b2c3d4.":
            self.mensagem["text"] = "Autenticado"
            sistema = tkinter.Toplevel(root)
            sistema.title("Opções de Cadastro")
            sistema.geometry("300x300")
            titulo_opçao = tkinter.Label(sistema, text="Escolha uma das Opções", font= self.fontePadrao)

            titulo_opçao.pack()

        else:
            self.mensagem["text"] = "Tente Novamente"
            
    #criando uma nova janela        
    def cadastrar(self):
        
        nova_janela = tkinter.Toplevel(root)
        nova_janela.title("Cadastro")
        nova_janela.geometry("300x300")
        
        self.titulo_cadastro = tkinter.Label(nova_janela, text="Cadastro ", font=self.fontePadrao, pady="10")
        
        self.titulo_nome_cadastro = tkinter.Label(nova_janela, text="Nome Completo: ")
        self.inserir_nome_cadastro = tkinter.Entry(nova_janela) 
        
        self.email_cadastro = tkinter.Label(nova_janela, text="Informe o Email: ")
        self.inserir_email_cadastro = tkinter.Entry(nova_janela)
        
        self.nome_usuario = tkinter.Label(nova_janela, text="Usuário")
        self.inserir_nome_usuario = tkinter.Entry(nova_janela)
        
        self.senha_cadastro = tkinter.Label(nova_janela, text="Senha")
        self.inserir_senha_cadastro = tkinter.Entry(nova_janela)
        
        confirmar = Button(nova_janela, text="Confirmar", command=self.InserirUsuario, padx="10")

        self.titulo_cadastro.pack()
        self.titulo_nome_cadastro.pack()
        self.inserir_nome_cadastro.pack()
        
        self.email_cadastro.pack()
        self.inserir_email_cadastro.pack()
        
        self.nome_usuario.pack()
        self.inserir_nome_usuario.pack()
        
        self.senha_cadastro.pack()
        self.inserir_senha_cadastro.pack()
        
        confirmar.pack()
        
    def InserirUsuario(self):
        user = Usuario()

        user.nome = self.inserir_nome_cadastro.get()
        user.email = self.inserir_email_cadastro.get()
        user.usuario = self.inserir_nome_usuario.get()
        user.senha = self.inserir_senha_cadastro.get()
        
        self.lblmsg["text"] = user.insertUser()
        
        self.inserir_nome_cadastro.delete(0, END)
        self.inserir_email_cadastro.delete(0, END)
        self.inserir_nome_usuario.delete(0, END)
        self.inserir_senha_cadastro.delete(0, END)



root = Tk()
Application(root)
root.mainloop()
