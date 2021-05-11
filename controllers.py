import uuid
from datetime import timedelta, datetime
from enum import Enum

from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal
from models import \
    insert_usuario, get_usuario, update_usuario, delete_usuario, select_usuarios, \
    insert_diretor, get_diretor, update_diretor, delete_diretor, select_diretores, \
    insert_genero, get_genero, update_genero, delete_genero, select_generos, \
    insert_filme, get_filme, update_filme, delete_filme, select_filmes, \
    select_locacao, insert_locacao, get_locacao, insert_pagamento, get_pagamento, get_preco
from serializadores import \
    usuario_from_web, usuario_from_db, nome_usuario_from_web, \
    diretor_from_web, diretor_from_db, nome_diretor_from_web, \
    genero_from_web, genero_from_db, nome_genero_from_web, \
    filme_from_web, filme_from_db, nome_filme_from_web, \
    locacao_from_web, locacao_from_db, pagamento_from_web, pagamento_from_db
from validacao import valida_usuario, valida_diretor, valida_genero, valida_filme, valida_locacao, valida_pagamento


app = Flask(__name__)


@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/diretores", methods=["POST"])
def inserir_diretores():
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor inválido"})

@app.route("/generos", methods=["POST"])
def inserir_generos():
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Genero inválido"})

@app.route("/filmes", methods=["POST"])
def inserir_filmes():
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme inválido"})

@app.route("/locacoes", methods=["POST"])
def inserir_locacao():
    locacao = locacao_from_web(**request.json)
    pagamento = pagamento_from_web(**request.json)
    filme = filme_from_web(**request.json)
    class Tipo(Enum):
        Credito = 1
        Debito = 2
        Paypal = 3

    class Status(Enum):
        Aprovado = 1
        EmAnalise = 2
        Reprovado = 3

    codigo_pagamento = uuid.uuid4()
    precofilme = get_preco(**filme)
    #############################################################################
    #NAO CONSEGUI PEGAR O PREÇO DO FILME PARA EXIBIR EM PAGAMENTO, AJUDAAAAAAAAA#
    #############################################################################
    #valor_locacao = get_preco(id_filme)
    hora_locacao = datetime.now()
    tempo_locacao = timedelta(hours=48, minutes=0, seconds=0)
    hora_final = hora_locacao + tempo_locacao
    if valida_locacao(**locacao):
        if valida_pagamento(**pagamento):
            id_locacao = insert_locacao(hora_locacao, hora_final, **locacao)
            id_pagamento = insert_pagamento(codigo_pagamento, precofilme, hora_locacao, **pagamento)
            locacao_cadastrada = get_locacao(id_locacao)
            pagamento_cadastrado = get_pagamento(id_pagamento)
            return jsonify(locacao_from_db(locacao_cadastrada)), jsonify(pagamento_from_db(pagamento_cadastrado))
        else:
            return jsonify({"erro": "Locação inválida"})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor inválido"})

@app.route("/generos/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Genero inválido"})

@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme inválido"})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})

@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return "", 204
    except:
        return jsonify({"erro": "Diretor possui itens conectados a ele"})

@app.route("/generos/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return "", 204
    except:
        return jsonify({"erro": "Genero possui itens conectados a ele"})

@app.route("/filmes/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return "", 204
    except:
        return jsonify({"erro": "Filme possui itens conectados a ele"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)

@app.route("/diretores", methods=["GET"])
def buscar_diretore():
    nome_completo = nome_diretor_from_web(**request.args)
    diretores = select_diretores(nome_completo)
    diretores_from_db = [diretor_from_db(diretor) for diretor in diretores]
    return jsonify(diretores_from_db)

@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome = nome_genero_from_web(**request.args)
    generos = select_generos(nome)
    generos_from_db = [genero_from_db(genero) for genero in generos]
    return jsonify(generos_from_db)

@app.route("/filmes", methods=["GET"])
def buscar_filme():
    titulo = nome_filme_from_web(**request.args)
    filmes = select_filmes(titulo)
    filmes_from_db = [filme_from_db(filme) for filme in filmes]
    return jsonify(filmes_from_db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)