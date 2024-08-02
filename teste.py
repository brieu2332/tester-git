import json# importa json para persistir o dado em json
from Person import Person
  
# main program -------------------------

# ask data
name = input('Please, give your name: ')
year_born = int(input('Give your borning year: '))
cpf = input('Give your CPF: ')

# create the object
someone = Person(name, year_born, cpf)

#pega as informações do objeto e salva num arquivo json
with open('Person.json', 'w') as f:
    json.dump(someone.toDict(), f)

# show the data
print(someone)