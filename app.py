# importações
from flask import *
from flask_cors import CORS

# configurando a aplicação
app = Flask(__name__)
CORS(app)  

# rotas
with app.app_context():
    @app.route("/")
    def inicio():
        return 'o sistema está em funcionamento!'
    
    @app.route("/listar")
    def listar():    
        try:
            resposta = open('Person.json') # utiliza o arquivo .json gerado pelo teste
        except Exception as e:
            resposta = jsonify({"resultado":"erro","detalhes":str(e)})
            print("ERRO: "+str(e))
        return resposta
    
    app.run(debug=True, host="0.0.0.0")