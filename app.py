from email import message

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/usuarios', methods=['GET'])
def buscar_usuarios():
    usuario = {
        "nome": "Nicolas",
        "idade": 19,
        "telefone": "(19) 988446677"
    }
    return usuario

@app.route('/produtos', methods=['POST'])
def cadastrar_produtos():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro":"Daods invalidos"}),400

    print(f"Novo produto:{dados}")
    return jsonify({
        'message':'produto cadastrado',
        "produto cadastrado":dados
    }), 200

@app.route('/produtos', methods=['PUT'])
def atualizar_produto():
    produto = {
    "id": 1,
    "nome": "caneta azul",
    "preco": 1.5,
    "descricao": "caneta esferografica",
    "marca": "BIC"

}

    dados = request.get_json()

    if not dados:
        return jsonify({"erro":"Daods invalidos"}),400

    if dados['id'] == produto['id']:
        produto = dados

        print(f"Atualização de  produto:{produto}")

        return jsonify({"message":"produto atualizado"}), 201

    else:
        return jsonify({"message":"produto nao encontrado"}), 404



if __name__ == '__main__':
    app.run(debug=True)


