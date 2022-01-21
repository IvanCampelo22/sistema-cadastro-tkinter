class Alunos:

    def __init__(self, nome, nome_mae, cpf, telefone):
        self.__nome = nome
        self.__nome_mae = nome_mae
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nome_mae(self):
        return self.__nome_mae

    @nome_mae.setter
    def nome_mae(self, nome_mae):
        self.__nome_mae = nome_mae

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

