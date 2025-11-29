import unittest
from set_add import contar_paises_distintos

class testSetAdd(unittest.TestCase):
    def test_paises_repetidos(self):
        self.assertEqual(contar_paises_distintos(["Uk", "usa", "Uk"]), 2)
    
    def test_sin_paises(self):
        self.assertEqual(contar_paises_distintos([]), 0)
    
    def test_todos_diferentes(self):
        self.assertEqual(contar_paises_distintos(["Francia", "España", "Italia"]), 3)


    if __name__ == "__main__":
        unittest.main()