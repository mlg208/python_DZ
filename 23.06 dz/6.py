def find_duplicate_employees(employees):
    unique_employees = set()
    duplicates = set()

    for employee in employees:
        if employee in unique_employees:
            duplicates.add(employee)
        else:
            unique_employees.add(employee)

    return duplicates

employee_list = ["Иванов", "Петров", "Сидоров", "Иванов", "Смирнов"]
duplicate_employees = find_duplicate_employees(employee_list)

print("Сотрудники, попавшие в базу дважды:", duplicate_employees)
