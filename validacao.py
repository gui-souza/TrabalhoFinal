from models import get_diretor

def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False

    return True

def valida_genero(nome):
    if len(nome) == 0:
        return False

    return True

def valida_filme(titulo, ano, classificacao, preco, **kwargs):
    if len(titulo) == 0:
        return False

    if len(ano) != 4:
        return False

    if len(classificacao) == 0:
        return False

    if len(preco) == 0:
        return False

    return True

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True
