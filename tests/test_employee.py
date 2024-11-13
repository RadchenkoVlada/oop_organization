import unittest
from models.employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def test_init_positive(self):
        e = Employee("Vlada", "Radchenko", 100.0, 12)
        self.assertEqual("Vlada", e.first_name)
        self.assertEqual("Radchenko", e.last_name)
        self.assertEqual(100.0, e.base_salary)
        self.assertEqual(12, e.experience)

    def test_init_negative(self):
        with self.assertRaises(TypeError):
            Employee(1, "Radchenko", 100.0, 12)
        with self.assertRaises(TypeError):
            Employee("Vlada", 1, 100.0, 12)
        with self.assertRaises(TypeError):
            Employee("Vlada", "Radchenko", "str", 12)
        with self.assertRaises(TypeError):
            Employee("Vlada", "Radchenko", 100.0, "str")

        with self.assertRaises(ValueError):
            Employee("", "Radchenko", 100.0, 12)
        with self.assertRaises(ValueError):
            Employee("Vlada", "", 100.0, 12)
        with self.assertRaises(ValueError):
            Employee("Vlada", "Radchenko", 100.0, -12)
        with self.assertRaises(ValueError):
            Employee("Vlada", "Radchenko", -4.5, 12)

    def test_get_counted_salary(self):
        e1 = Employee("Vlada", "Radchenko", 100.0, 2)
        self.assertEqual(100.0, e1.get_counted_salary())
        e2 = Employee("Anna", "Bara", 150.3, 3)
        self.assertEqual(350.3, e2.get_counted_salary())
        e3 = Employee("Anna", "Bara", 42.0, 5)
        self.assertEqual(242.0, e3.get_counted_salary())
        e4 = Employee("Anna", "Bara", 42.0, 6)
        self.assertEqual(550.4, e4.get_counted_salary())

