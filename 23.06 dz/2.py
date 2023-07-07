numbers_list = [3, 9, 8, 4, 5, 1]
result_list = []

for i in range(1, len(numbers_list)):
    if numbers_list[i] > numbers_list[i-1]:
        result_list.append(numbers_list[i])

print("Элементы, которые больше предыдущих элементов:", result_list)
