import json

class MyClass:
    def __init__(self, name, value, cpf):
        self.name = name
        self.value = value
        self.cpf = cpf

    def to_dict(self):
        return {'name': self.name, 'value': self.value, 'cpf':self.cpf}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['value'], data['cpf'])

# Criando uma instância da classe
obj = MyClass('example', 42, 123)

# Salvando o objeto em um arquivo JSON
with open('myclass.json', 'w') as f:
    json.dump(obj.to_dict(), f)
from datetime import date #para saber a data atual

#voce esta na branch master


#variaveis
anoAtual = date.today().year #coloca o ano atual dentro da vari ano
nome = ""
anoDeNascimento = 0
calculoIdade = 0

#entrada
nome = input('diga seu nome:')
anoDeNascimento = int(input('coloque sua data de nascimento:'))

# Carregando o objeto do arquivo JSON
with open('myclass.json', 'r') as f:
    data = json.load(f)
    loaded_obj = MyClass.from_dict(data)

print(loaded_obj.name, loaded_obj.value, loaded_obj.cpf)
