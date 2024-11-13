import unittest
from models.designer import Designer

class DesignerTestCase(unittest.TestCase):
    def test_init_positive(self):
        e = Designer("Vlada", "Radchenko", 100.0, 12, 0.5)
        self.assertEqual("Vlada", e.first_name)
        self.assertEqual("Radchenko", e.last_name)
        self.assertEqual(100.0, e.base_salary)
        self.assertEqual(12, e.experience)


    def test_init_negative(self):
        with self.assertRaises(TypeError):
            Designer("B", "Radchenko", 100.0, 12, 1)
        with self.assertRaises(ValueError):
            Designer("Olga", "Radchenko", 100.0, 12, -0.1)
        with self.assertRaises(ValueError):
            Designer("Vlada", "Radchenko", 100.0, 12, 1.1)

    def test_get_counted_salary(self):
        e1 = Designer("Vlada", "Radchenko", 100.0, 2, 0.5)
        self.assertEqual(50.0, e1.get_counted_salary())
        e2 = Designer("A", "B", 100.0, 2, 0.0)
        self.assertEqual(0.0, e2.get_counted_salary())

