from email import message

from flask import Flask, request, jsonify, render_template, redirect, url_for
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
        INSERT INTO filmeS (usuario_id, titulo, ano_lançamento,
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

@app.route('/deletar/<int:id>', methods=['POST'])
def delete(id):
   conn = criar_conexao()
   cursor = conn.cursor()
   cursor.execute("DELETE FROM filmes WHERE id = %s", (id,))
   conn.commit()
   conn.close()
   return redirect(url_for("listar_filmes"))

@app.route('/novo', methods=["GET", "POST"])
def novo_filme():
    if request.method == "POST":
        titulo = request.form["titulo"]
        genero = request.form["genero"]
        capa_url = request.form["capa_url"]
        nota = request.form["nota"]
        ano_lancamento_form = request.form.get("ano_lancamento") or request.form.get("ano_lançamento")
        usuario_id = 1

        parametros = [titulo, genero, capa_url, nota, ano_lancamento_form, usuario_id]

        sql = '''
        INSERT INTO filmes (titulo, genero, capa_url, nota, ano_lançamento, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(sql, parametros)
        conn.commit()
        conn.close()
        return redirect(url_for("listar_filmes"))

    return render_template('novo_filme.html')

@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    print('Criando conexao:', conn)
    conn.close()
    return jsonify({"message": "Banco conectado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)