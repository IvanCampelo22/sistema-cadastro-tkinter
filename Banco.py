import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
    
    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios,
                    nome text, 
                    email text, 
                    usuario text, 
                    senha intenger""")
        self.conexao.commit()
        c.close()