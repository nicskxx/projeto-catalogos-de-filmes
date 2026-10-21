from email import message


from flask import Flask, request, jsonify, render_template
from psycopg2.extras import RealDictCursor

from database import criar_conexao

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/filme', methods=['GET'])
def listar_filmes():
    conn = criar_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("SELECT * FROM filmes")
    resultado = cursor.fetchall()

    conn.close()

    return render_template("index.html", filmes=resultado)

@app.route('/filme', methods=['POST'])
def cadastrar_filme():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro":"Daods invalidos"}),400

    print(f"Novo filme:{dados}")

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO filmeS (usuario_id, titulo,ano_lançamento,
         genero, nota, capa_url) 
         VALUES( %s, %s, %s, %s, %s, %s)
         RETURNING id;
         
        ''',
        (dados['usuario_id'], dados['titulo'], dados['ano_lançamento'],
         dados['genero'], dados['nota'], dados['capa_url'])


    )

    novo_id = cursor.fetchone()[0]
    conn.commit()
    conn.close()




    return jsonify({
        'message':'filme cadastrado',
        "filme cadastrado":dados

    }), 200

@app.route('/filme', methods=['PUT'])
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




@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Criando conexao:', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso!"}), 200







if __name__ == '__main__':
    app.run(debug=True)


