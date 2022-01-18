from alunos_cadastro import Alunos


def listar_alunos():
    lista_alunos = list()
    try:
        with open("alunos.txt", "r") as arquivo:
            lista_alunos_arquivo = arquivo.readlines()
            for i in lista_alunos_arquivo:
                dados = (i.split('-'))
                alunos_arquivo = Alunos(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
                lista_alunos.append(alunos_arquivo)
            return lista_alunos
    except FileNotFoundError:
        print("Arquivo não encontrado")


def cadastrar_alunos(aluno_novo):
    try:
        if buscar_aluno_cpf(aluno_novo.cpf):
            return False
        else:
            with open("contatos.txt", "a") as arquivo:
                arquivo.write(
                    f"{aluno_novo.nome} - {aluno_novo.cpf} - {aluno_novo.nome_mae} - {aluno_novo.telefone} \n")
                return True
    except FileNotFoundError:
        print("Arquivo não encontrado")


def buscar_aluno(cpf_aluno):
    try:
        with open("alunos.txt", "r") as arquivo:
            lista_alunos = arquivo.readlines()
            for i, linha in enumerate(lista_alunos):
                dados = (linha.split('-'))
                if dados[1][1: -1] == cpf_aluno:
                    return i
                else:
                    return -1
    except FileNotFoundError:
        print("Arquivo não encontrado")


def buscar_aluno_cpf(cpf_aluno):
    try:
        linha = buscar_aluno(cpf_aluno)
        if linha >= 0:
            with open("alunos.txt") as arquivo:
                lista_alunos = arquivo.readlines()
                dados = lista_alunos[linha].split('-')
                aluno_encontrado = Alunos(dados[0][:-1], dados[1][1:-1], dados[2][1:-1])
            return aluno_encontrado
    except FileNotFoundError:
        print("Arquivo não encontrado")


def remover_aluno_cpf(cpf_aluno):
    try:
        linha = buscar_aluno(cpf_aluno)
        if linha >= 0:
            with open("alunos.txt", "r") as arquivo:
                lista_alunos = arquivo.readlines()
                alunos = list()
                for i, linha_aluno in enumerate(lista_alunos):
                    if i != linha:
                        alunos.append((linha_aluno))
            with open("alunos.txt", "w") as arquivo:
                arquivo.writelines((alunos))
            return True
        else:
            return False
    except FileNotFoundError:
        print("Arquivo não encontrado")
