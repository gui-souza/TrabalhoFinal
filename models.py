from main import insert, select, update, delete, select_like, query
from datetime import timedelta, datetime

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)

def insert_diretor(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]

def update_diretor(id_diretor, nome_completo):
    update("diretores", "id", id_diretor, ["nome_completo"], [nome_completo])

def delete_diretor(id_diretor):
    delete("diretores", "id", id_diretor)

def select_diretores(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)

def insert_genero(nome):
    return insert("generos", ["nome"], [nome])

def get_genero(id_diretor):
    return select("generos", "id", id_diretor)[0]

def update_genero(id_diretor, nome):
    update("generos", "id", id_diretor, ["nome"], [nome])

def delete_genero(id_diretor):
    delete("generos", "id", id_diretor)

def select_generos(nome):
    return select_like("generos", "nome", nome)

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
                  [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]

def update_filme(id_filme, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])

def delete_filme(id_filme):
    delete("filmes", "id", id_filme)

def select_filmes(titulo):
    return select_like("filmes", "titulo", titulo)

def insert_locacao(data_inicio, data_fim, filmes_id, usuarios_id):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "usuarios_id"],
                  [data_inicio, data_fim, filmes_id, usuarios_id])

def insert_pagamento(codigo_pagamento, valor, data, tipo, status, locacoes_id):
    return insert("pagamento", ["codigo_pagamento", "valor", "data", "tipo", "status", "locacoes_id"],
                  [codigo_pagamento, valor, data, tipo, status, locacoes_id])

def select_locacao():
    return query("SELECT filmes.titulo FROM filmes INNER JOIN locacoes WHERE filmes.id = locacao.id")

def get_locacao(id_locacao):
    return select("locacoes", "id", id_locacao)[0]

def get_pagamento(id_pagamento):
    return select("pagamento", "id", id_pagamento)[0]

def get_preco(preco, **kwargs):
    return select("filmes", "preco", preco)