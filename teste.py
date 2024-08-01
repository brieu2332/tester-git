from datetime import date 
import json# importa json para persistir o dado em json

# class definition ---------------------
class Person:
    def __init__(self, name, year_born, cpf):
        self.name = name
        self.year_born = year_born
        self.cpf = cpf

    def __str__(self):
        return f'''{self.name}, born in {self.year_born} (age: {date.today().year-self.year_born}), 
CPF: {self.cpf}'''
    
    def toDict(self):
        return {'name': self.name, 'year_born': self.year_born, 'cpf': self.cpf}#passa quais informações serao salvas
    
   
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