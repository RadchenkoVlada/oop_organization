class Employee:

    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be str type")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be str type")
        if not isinstance(base_salary, float):
            raise TypeError("base_salary must be float type")
        if not isinstance(experience, int):
            raise TypeError("experience must be int type")

        if not first_name or not last_name:
            raise ValueError("first_name and last_name should be not empty strings")

        if base_salary < 0:
            raise ValueError("base_salary must be positive")
        if experience < 0:
            raise ValueError("experience must be positive")

        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience



    def get_counted_salary (self):
        """Calculate employee's salary based on base salary"""
        if self.experience > 5:
            return self.base_salary * 1.2 + 500
        if self.experience > 2:
            return self.base_salary + 200
        return self.base_salary






