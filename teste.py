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

# Carregando o objeto do arquivo JSON
with open('myclass.json', 'r') as f:
    data = json.load(f)
    loaded_obj = MyClass.from_dict(data)

print(loaded_obj.name, loaded_obj.value, loaded_obj.cpf)
