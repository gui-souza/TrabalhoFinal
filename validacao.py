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

    ####################CRIAR VALIDAÇÃO PARA PEGAR ID_DIRETOR, ID_GENERO######################

    return True

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True

def valida_locacao(filmes_id, usuarios_id):
    if len(filmes_id) == 0:
        return False

    if len(usuarios_id) == 0:
        return False

    return True

def valida_pagamento(tipo, status):
    if len(tipo) == 0:
        return False

    if len(status) == 0:
        return False



    return True


