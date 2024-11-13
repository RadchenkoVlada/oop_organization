# Department Management System

## Requirements

### Task 1:
Create an object model of the organization. There should be three types of Employee
in the organization: Developer , Designer and Manager . Each employee must have the
following fields:
- `first_name`
- `last_name`
- `base_salary`
- `experience`(in years)

**Each type of employee has additional fields:**
- **Designer:** additional field `efficiency coefficient` (`eff_coeff`) -a number
between 0 and 1.
- **Manager:** optional field `team` - a list consisting of an arbitrary number of
`Developer` and `Designer`.
The salary calculation is based on experience and specific rules for each employee type.
- A **Department** object contains:
A list of `Manager` objects, each with a team of employees.

Department should have a method `give_salary()`, which calculates and prints each employee's salary in the format:

`<first_name> <last_name> received <salary> money `.

**Calculation of `counted_salary` for each type of employee:**
- **General rules for all employees:**
- If experience > 2 years: `base_salary + 200`
- If experience > 5 years: `base_salary * 1.2 + 500`

**Designer:** 
`counted_salary * eff_coeff`

**Manager:** 
- If there are more than 5 people in the team:: `counted_salary + 200`
- If there are more than 10 people in the team: `counted_salary + 300`
- If more than half of Developers are in the team, the salary increases
by another 10%.

### Task 2:
Add two methods to department:
- `save_employees()`:
1. Should serialize the entire list of managers (with employees) and save
it to JSON file.
2. File name should be passed as argument.
- `load_employees()`:
1. Should load the JSON file, deserialize the data and add the managers
(with employees) to its list of managers.
2. File name should be passed as argument.
3. Handle error if file is not found.

### Task 3:
Write unit tests.
