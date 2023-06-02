total_sales = float(input("Введите общую сумму продаж за месяц: "))
try:
    base_salary = 250  
    commission = 0.1 * total_sales 
except ValueError:
    message = "это не цифры, введите именно цифры"
else:
    salary = base_salary + commission  
print("Зарплата работника составляет:", salary)