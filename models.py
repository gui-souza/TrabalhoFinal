from main import insert, select, update, delete, select_like

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
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])

def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]

def update_filme(id_filme, titulo, ano, classificacao, preco):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco"], [titulo, ano, classificacao, preco])

def delete_filme(id_filme):
    delete("filmes", "id", id_filme)

def select_filmes(titulo):
    return select_like("filmes", "titulo", titulo)