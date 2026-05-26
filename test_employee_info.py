import employee_info

def test_get_employees_by_age_range(): 
    result = []
    lower_limit = 20 
    upper_limit = 25 
    ans = [{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result = employee_info.get_employees_by_age_range(lower_limit, upper_limit)

    assert (result == ans) 

def test_calculate_average_salary(): 
    result = []
    ans = 60166.67
    result = employee_info.calculate_average_salary()

    assert result == ans 

def test_get_employees_by_dept(): 
    result = [] 
    dept = "Sales"
    ans = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
           {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_dept(dept)

    assert result == ans 