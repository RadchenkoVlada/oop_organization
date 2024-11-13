import unittest
import os
from models.designer import Designer
from models.manager import Manager
from models.developer import Developer
from models.department import Department
from unittest import mock


class DepartmentTestCase(unittest.TestCase):
    test_data_path = os.path.dirname(os.path.abspath(__file__))

    def test_init_positive(self):
        d1 = Department([Manager("Vlada", "Radchenko", 100.0, 12)])
        self.assertEqual(1, len(d1.managers))
        self.assertIsInstance(d1.managers[0], Manager)
        d2 = Department([])
        self.assertEqual([], d2.managers)
        d3 = Department()
        self.assertEqual([], d3.managers)

    def test_init_negative(self):
        with self.assertRaises(TypeError):
            d = Department(12)
        with self.assertRaises(TypeError):
            d = Department([42])

    def test_give_salary(self):
        mock_employee = mock.MagicMock(spec=Developer)
        mock_employee.first_name = "Vlada"
        mock_employee.last_name = "Radchenko"
        mock_employee.get_counted_salary.return_value = 500
        mock_manager = mock.MagicMock(spec=Manager)
        mock_manager.first_name = "Vlada"
        mock_manager.last_name = "Radchenko"
        mock_manager.get_counted_salary.return_value = 1000
        mock_manager.team = [mock_employee]

        d = Department([mock_manager])

        salary_info = """Vlada Radchenko received 1000 money.
Vlada Radchenko received 500 money.
"""
        self.assertEqual(salary_info, d.give_salary())


    def test_save_employees(self):
        d = Department([
            Manager("Man", "Manager", 100.0, 12,
                    [Designer("Des", "Des", 100.0, 12, 0.5), Developer("Dev", "Dev", 100.0, 12) ]),
            Manager("Man 2", "Manager 2", 100.0, 12,
                    [Designer("Des 2", "Des 2", 100.0, 12, 0.5), Developer("Dev 2", "Dev 2", 100.0, 12),
                      Developer("Dev 23", "Dev 23", 100.0, 12)])
        ])
        out_file = DepartmentTestCase.test_data_path + "/test_data/out_file.json"
        expected_file = DepartmentTestCase.test_data_path + "/test_data/example.json"
        d.save_employees(out_file)
        with open(out_file, 'r') as f:
            out_file_data = f.read()
        with open(expected_file, 'r') as f:
            expected_data = f.read()
        self.assertEqual(expected_data, out_file_data)
        os.remove(out_file)

    def test_load_employees(self):
        d = Department()
        in_file = DepartmentTestCase.test_data_path + "/test_data/example.json"
        d.load_employees(in_file)
        self.assertEqual(2, len(d.managers))
        self.asser_equal_fields_employees(Manager("Man", "Manager", 100.0, 12), d.managers[0])
        self.asser_equal_fields_employees(Manager("Man 2", "Manager 2", 100.0, 12), d.managers[1])

        self.assertEqual(2, len(d.managers[0].team))
        self.asser_equal_fields_employees(Designer("Des", "Des", 100.0, 12, 0.5), d.managers[0].team[0])
        self.asser_equal_fields_employees(Developer("Dev", "Dev", 100.0, 12), d.managers[0].team[1])

        self.assertEqual(3, len(d.managers[1].team))
        self.asser_equal_fields_employees(Designer("Des 2", "Des 2", 100.0, 12, 0.5), d.managers[1].team[0])
        self.asser_equal_fields_employees(Developer("Dev 2", "Dev 2", 100.0, 12), d.managers[1].team[1])
        self.asser_equal_fields_employees(Developer("Dev 23", "Dev 23", 100.0, 12), d.managers[1].team[2])


    def asser_equal_fields_employees(self, expected, actual):
        self.assertEqual(type(expected), type(actual))
        self.assertEqual(expected.first_name, actual.first_name)
        self.assertEqual(expected.last_name, actual.last_name)
        self.assertEqual(expected.base_salary, actual.base_salary)
        self.assertEqual(expected.experience, actual.experience)
        if isinstance(expected, Designer) and isinstance(actual, Designer):
            self.assertEqual(expected.eff_coeff, actual.eff_coeff)
