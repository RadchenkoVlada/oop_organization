import json
from models.employee import Employee
from models.designer import Designer
from models.manager import Manager
from models.developer import Developer
from models.department import Department


class SimpleEmployeeEncoder(json.JSONEncoder):
    def default(self, employee):
        if isinstance(employee, (Employee, Developer, Designer)):
            return employee.__dict__
        # Let the base class default method raise the TypeError
        return super().default(employee)


class ManagerEncoder(json.JSONEncoder):
    def default(self, employee):
        if isinstance(employee, Manager):
            return {'manager': {k: v for (k, v) in employee.__dict__.items() if k != 'team'},
                   'team': [ SimpleEmployeeEncoder().default(employee) for employee in employee.team ]}
        # Let the base class default method raise the TypeError
        return super().default(employee)


class DepartmentEncoder(json.JSONEncoder):
    def default(self, employee):
        if isinstance(employee, Department):
            return {'teams': [ManagerEncoder().default(manager) for manager in employee.managers]}
        # Let the base class default method raise the TypeError
        return super().default(employee)


class DepartmentDecoder(json.JSONDecoder):
    @staticmethod
    def decode_employee_info(employee_info):
        if 'eff_coeff' in employee_info:
            return Designer(**employee_info)
        return Developer(**employee_info)

    def decode(self, s):
        data = json.loads(s)
        managers = []
        for manager_info in data['teams']:
            manager = Manager(**manager_info['manager'], team=[DepartmentDecoder.decode_employee_info(info) for info in manager_info['team']])
            managers.append(manager)
        return Department(managers)
