from models.manager import Manager
from typing import List, Optional
import json
from json import JSONDecoder

```
class Department:
    def __init__(self, managers: Optional[List[Manager]] = None):
        if managers is None:
            managers = []
        if not isinstance(managers, list):
            raise TypeError("manager must be list type")
        if any([not isinstance(e, Manager) for e in managers]):
            raise TypeError("managers must be a list of Managers. Other types are not allowed in the list")
        self.managers = managers

    def print_salary(self):
        print(self.give_salary())

    def give_salary(self):
        result = ""
        for manager in self.managers:
            result += Department.generate_employee_information_line(manager) + '\n'
            for e in manager.team:
                result += Department.generate_employee_information_line(e) + '\n'
        return result

    @staticmethod
    def generate_employee_information_line(employee) -> str:
        return f"{employee.first_name} {employee.last_name} received {round(employee.get_counted_salary())} money."

    def save_employees(self, filename):
        from models.serialization import DepartmentEncoder
        data = json.dumps(self, cls=DepartmentEncoder)
        try:
            with open(filename, 'w') as f:
                f.write(data)
        except OSError as e:
            print("Can't save employees to file. OS Error:", e)


    def load_employees(self, filename):
        from models.serialization import DepartmentDecoder
        try:
            with open(filename, 'r') as f:
                data = f.read()
            self.managers = json.loads(data, cls=DepartmentDecoder).managers
        except OSError as e:
            print("Can't load employees from file. OS Error:", e)

