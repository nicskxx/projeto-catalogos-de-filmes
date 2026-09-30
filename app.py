from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World!'

@app.route('/usuarios')
def buscar_usuarios():
    usuario = {
        "nome": "Nicolas",
        "idade": 16,
        "telefone": "(19) 988446677"
    }
    return usuario





if __name__ == '__main__':
    app.run(debug=True)


