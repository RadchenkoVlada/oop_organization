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


    TEST_CASES = [
        ("Vlada", "Radchenko", 100.0, 2, 100.0),
        ("Anna", "Bara", 150.3, 3, 350.3),
        ("Anna", "Bara", 42.0, 5, 242.0),
        ("Anna", "Bara", 42.0, 6, 550.4)
    ]

    def test_get_counted_salary(self):
        for first_name, last_name, base_salary, experience, expected_salary in self.TEST_CASES:
            with self.subTest(base_salary=base_salary, experience=experience):
                employee = Employee(first_name, last_name, base_salary, experience)
                self.assertEqual(employee.get_counted_salary(), expected_salary)


