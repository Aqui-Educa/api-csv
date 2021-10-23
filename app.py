import csv
from flask import Flask

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

@app.route("/incluir/")
def incluir():
    with open('cadastro.csv', 'a', newline='') as cad:
        escrever = csv.writer(cad, delimiter= ',')
        usuario = ['4', 'luis', '8485415']
        escrever.writerow(usuario)

    return 'ok'