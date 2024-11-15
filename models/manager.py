from models.developer import Developer
from models.designer import Designer
from models.employee import Employee
from typing import List, Optional, Union


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, team: Optional[List[Developer | Designer]] = None):
        """Initialize Manager with optional team of Developers and Designers"""
        super().__init__(first_name, last_name, base_salary, experience)
        self.team = self._validate_team(team)



    def _validate_team(self, team: Optional[List[Union[Developer, Designer]]]) -> List[Union[Developer, Designer]]:
        """Validate and return team list"""
        if team is None:
            return []
        if not isinstance(team, list):
            raise TypeError("team must be of a list type")
        if not all(isinstance(member, (Developer, Designer)) for member in team):
            raise TypeError("team must contain only Developers and Designers")
        return team


    def get_counted_salary(self):
        """Calculate manager's salary based on team structure"""
        salary = super().get_counted_salary()

        team_size = len(self.team)
        if team_size > 10:
            salary += 300
        if team_size > 5:
            salary += 200

        if team_size > 0:
            developer_ratio = self._get_developer_ratio()
            if developer_ratio > 0.5:
                salary *= 1.1

        return salary


    def _get_developer_ratio(self) -> float:
        """Calculate ratio of developers in the team"""
        if not self.team:
            return 0.0
        developers_count = sum(isinstance(member, Developer) for member in self.team)
        return developers_count / len(self.team)




