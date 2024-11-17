from models.employee import Employee


class Designer(Employee):
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int, eff_coeff: float):
        super().__init__(first_name, last_name, base_salary, experience)
        self.eff_coeff = self._validate_eff_coeff(eff_coeff)

    def _validate_eff_coeff(self, eff_coeff: float):
        if not isinstance(eff_coeff, float):
            raise TypeError("Efficiency coefficient must be float")
        if eff_coeff < 0 or eff_coeff > 1:
            raise ValueError("Efficiency coefficient must be between 0 and 1")
        return eff_coeff

    def get_counted_salary(self):
        return super().get_counted_salary() * self.eff_coeff

