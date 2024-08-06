# importações
from flask import *
from flask_cors import CORS
from Person import *

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
       
    @app.route("/cadastrar", methods=['post'])
    def cadastrar():
        # reference: 
        # https://gitlab.com/hvescovi/prog23/-/blob/main/web/python_js/03-post/server.py

        # load the new data
        newdata = request.get_json()

        try:
            # load data from database
            try:
                with open('Person.json', 'r') as f:
                    data = json.load(f)
                    if not isinstance(data, list):
                        data = [data]
            except FileNotFoundError:
                data = []

            # create the new person
            new = Person(**newdata)

            # get the person in json format
            newj = new.to_dict()

            # add the person to the current database
            data.insert(0, newj)

            # update the database
            with open('Person.json', 'w') as f:
                json.dump(data, f, indent=4)

            return jsonify({"resultado": "ok", "detalhes": "ok"}) 
        
        except Exception as e: # em caso de erro...
            # informar mensagem de erro
            return jsonify({"resultado": "erro", "detalhes": str(e)}) 
    
    app.run(debug=True, host="0.0.0.0")

    '''
    example:

$ curl localhost:5000/cadastrar -X POST -d '{"name":"John Stick", "year_born":2000,"cpf":"06916689730"}' -H "Content-Type:application/json"
{
  "detalhes": "ok",
  "resultado": "ok"
}

$ curl localhost:5000/listar
[
    {
        "age": 24,
        "cpf": "06916689730",
        "name": "John Stick",
        "year_born": 2000
    },
    {
        "age": 2005,
        "cpf": "320498",
        "name": "gabriel",
        "year_born": 19
    },
    {
        "age": 1984,
        "cpf": "3248907",
        "name": "teste final",
        "year_born": 40
    },
    {
        "age": 1890,
        "cpf": "1340193",
        "name": "teste2",
        "year_born": 134
    },
    {
        "age": -7810,
        "cpf": "28374",
        "name": "hsdgfv",
        "year_born": 9834
    },
    {
        "age": 1992,
        "cpf": "3124",
        "name": "teste3",
        "year_born": 32
    }
]

    '''