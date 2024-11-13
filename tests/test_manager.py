import unittest
from models.designer import Designer
from models.manager import Manager
from models.developer import Developer


class ManagerTestCase(unittest.TestCase):
    def test_init_positive(self):
        e = Manager("Vlada", "Radchenko", 100.0, 12)
        self.assertEqual("Vlada", e.first_name)
        self.assertEqual("Radchenko", e.last_name)
        self.assertEqual(100.0, e.base_salary)
        self.assertEqual(12, e.experience)
        self.assertEqual([], e.team)

        e1 = Manager("Vlada", "Radchenko", 100.0, 12, [])
        self.assertEqual([], e1.team)

        e2 = Manager("Vlada", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1), Developer("Vlad", "A", 100.0, 12)])
        self.assertEqual(2, len(e2.team))
        self.assertIsInstance(e2.team[0], Designer)
        self.assertIsInstance(e2.team[1], Developer)


    def test_init_negative(self):
        with self.assertRaises(TypeError):
            Manager("B", "Radchenko", 100.0, 12, "")
        with self.assertRaises(TypeError):
            Manager("B", "Radchenko", 100.0, 12, 42)
        with self.assertRaises(TypeError):
            Manager("B", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1), 42])

    def test_get_counted_salary(self):
        m = Manager("B", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1)] * 5)
        self.assertEqual(620.0, m.get_counted_salary())
        m = Manager("B", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1)] * 6)
        self.assertEqual(820.0, m.get_counted_salary())
        m = Manager("B", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1)] * 10)
        self.assertEqual(820.0, m.get_counted_salary())
        m = Manager("B", "Radchenko", 100.0, 12, [Designer("Vlada", "A", 100.0, 12, 0.1)] * 11)
        self.assertEqual(920.0, m.get_counted_salary())
        m = Manager("B", "Radchenko", 100.0, 12,
                    [Developer("Vlada", "A", 100.0, 12)] * 6 +
                    [Designer("Vlada", "A", 100.0, 12, 0.1)] * 5)
        self.assertAlmostEqual(1012.0, m.get_counted_salary())
