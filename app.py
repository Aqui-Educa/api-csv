import csv
from os import write
from flask import Flask, request

app = Flask(__name__)

@app.route("/<id>", methods=['GET'])
def listar(id):
    with open('cadastro.csv', 'r', encoding='utf-8') as cad:
        tabela = csv.reader(cad, delimiter=',')
        for linha in tabela:
            if linha[0] == id:
                usuario = {
                    "id": linha[0],
                    "nome": linha[1],
                    "documento": linha[2]
                }
                return usuario

    return 'Usuário não encontrado.'

@app.route("/incluir/", methods=['POST'])
def incluir():
    user_info = request.json
    with open('cadastro.csv', 'a', newline='') as cad:
        escrever = csv.writer(cad, delimiter= ',')
        usuario = [user_info['id'], user_info['nome'], user_info['documento']]
        escrever.writerow(usuario)

    return 'ok'

@app.route("/deletar/<id>", methods=['DELETE'])
def deletar(id):
    # Abre o arquivo para leitura
    with open("cadastro.csv", "r", encoding="utf-8") as cad:
        # leitura do arquivo csv
        leitura = csv.reader(cad, delimiter=',')

        # armazena o conteudo do csv na variavel
        data = list(leitura)
    
    # Abre o arquivo para escrita
    with open("cadastro.csv", "w", encoding="utf-8") as cad:
        # objeto de escrita
        escrita = csv.writer(cad, delimiter=',')

        for linha in data:
            codigo = linha[0]

            if codigo != id:
                escrita.writerow(linha)

    return 'ok'
