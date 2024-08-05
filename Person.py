from datetime import date 

class Person:
    def __init__(self, name, year_born, cpf):
        self.name = name
        self.year_born = year_born
        self.cpf = cpf
        self.age = date.today().year - self.year_born

    def __str__(self):
        return f'''{self.name}, born in {self.year_born} (age: {self.age}),CPF: {self.cpf}'''
    
    def to_dict(self):
        return {'name': self.name, 'year_born': self.year_born, 'cpf': self.cpf, 'age': self.age}#passa quais informações serao salvas
    
 