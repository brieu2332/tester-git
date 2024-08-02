from datetime import date 

class Person:
    def __init__(self, name, year_born, cpf):
        self.name = name
        self.year_born = year_born
        self.cpf = cpf

    def __str__(self):
        return f'''{self.name}, born in {self.year_born} (age: {date.today().year-self.year_born}),CPF: {self.cpf}'''
    
    def toDict(self):
        return {'name': self.name, 'year_born': self.year_born, 'cpf': self.cpf}#passa quais informações serao salvas
    
 