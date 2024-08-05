import json# importa json para persistir o dado em json
from Person import Person
from datetime import date

# main program -------------------------

# ask data
name = input('Please, give your name: ')
year_born = int(input('Give your borning year: '))
cpf = input('Give your CPF: ')

# create the object
someone = Person(name, year_born, cpf)

someone_data = someone.to_dict()

# Read the existing data from the JSON file
try:
    with open('Person.json', 'r') as f:
        data = json.load(f)
        if not isinstance(data, list):
            data = [data]
except FileNotFoundError:
    data = []

# Append the new data
data.insert(0, someone_data)

#pega as informações do objeto e salva num arquivo json
with open('Person.json', 'w') as f:
    json.dump(data, f, indent=4)

# show the data
print(someone)