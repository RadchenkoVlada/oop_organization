from models.developer import Developer
from models.designer import Designer
from models.employee import Employee
from typing import List, Optional


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, team: Optional[List[Developer | Designer]] = None):
        super().__init__(first_name, last_name, base_salary, experience)
        if team is None:
            self.team = []
        else:
            if not isinstance(team, list):
                raise TypeError("team must be of a list type")
            if any([not isinstance(e, (Developer, Designer)) for e in team]):
                raise TypeError("team must be a list of Developers and Designers. Other types are not allowed in the list")
            self.team = team


    def get_counted_salary(self):
        salary = super().get_counted_salary()
        num_team_members = len(self.team)
        if 5 < num_team_members <= 10:
            salary = salary + 200
        elif num_team_members > 10:
            salary = salary + 300

        num_developers = sum(isinstance(member, Developer) for member in self.team)
        if num_developers/num_team_members > 0.5:
            salary = salary * 1.1
        return salary

