from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: alice\n"
        "Employee id: E1001\n"
        "Department : IT\n"
        "salary: 55000\n"
    )

    assert employee_details("alice", "E1001", "IT", 55000) == expected_output

