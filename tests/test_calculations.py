import unittest
from ia.core.calculations import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Prépare un environnement de test propre avant chaque test.
        """
        self.calculator = Calculator()

    def test_complex_calculation(self):
        """
        Teste le calcul complexe (distance euclidienne).
        """
        result = self.calculator.complex_calculation(3, 4)
        self.assertEqual(result, 5.0)  # 3² + 4² = 5 (Pythagore)

    def test_average(self):
        """
        Teste le calcul de la moyenne d'une liste de nombres.
        """
        numbers = [10, 20, 30, 40]
        result = self.calculator.average(numbers)
        self.assertEqual(result, 25.0)

    def test_average_empty_list(self):
        """
        Teste le cas où la liste pour la moyenne est vide.
        """
        with self.assertRaises(ValueError) as context:
            self.calculator.average([])
        self.assertEqual(str(context.exception), "La liste des nombres est vide.")

    def test_optimize_process(self):
        """
        Teste l'optimisation d'un processus (tri des données).
        """
        data = [5, 3, 8, 1]
        result = self.calculator.optimize_process(data)
        self.assertEqual(result, [1, 3, 5, 8])

if __name__ == "__main__":
    unittest.main()