from Banco import *

class Usuario(object):

    def __init__(self, idusuario = 0, nome = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome 
        self.email = email 
        self.usuario = usuario
        self.senha = senha 
    
    def insertUser(self):

        banco = Banco()
        try: 

            c = banco.conexao.cursor()

            c.execute("insert into usuarios (nome, email, usuario, senha) values ('" + self.nome + "', '" +  "' , '" + self.email + "' , '" +
            self.usuario + "','" + self.senha + "' )")

            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucess!"
        
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "' , "' email = "' + self.email + "', "' usuario = "' + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conexao.commit()
            c.close()

            return "Usuario excluido com sucesso!"
        except:
            return "Ocorreu um erro na exlusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("select * from usuarios where idusuario = " + idusuario + " ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!" 
        except:
            return "Ocorreu um erro na busca do usuário"
        