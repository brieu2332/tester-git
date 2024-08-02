import unittest
from datetime import date
from Person import Person  # Substitua 'your_module' pelo nome do seu módulo

class TestPerson(unittest.TestCase):

    def setUp(self):
        # Método que é chamado antes de cada teste
        self.person = Person("João Silva", 1990, "123.456.789-00")

    def test_to_dict_method(self):
        # Testa o método toDict
        expected_dict = {'name': 'João Silva', 'year_born': 1990, 'cpf': '123.456.789-00'}
        self.assertEqual(self.person.toDict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
