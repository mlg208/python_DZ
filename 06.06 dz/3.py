def multiply_table(number):
    print("Таблица умножения для", number)
    for i in range(1, 11):
        result = number * i
        print("{} x {} = {}".format(number, i, result))
    print()  

def print_multiplication_tables():
    for number in range(2, 10):
        multiply_table(number)
print_multiplication_tables()
