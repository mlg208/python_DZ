numbers_list = [3, 9, 8, 4, 5, 1]

min_index = numbers_list.index(min(numbers_list))
max_index = numbers_list.index(max(numbers_list))

numbers_list[min_index], numbers_list[max_index] = numbers_list[max_index], numbers_list[min_index]

print("Измененный список:", numbers_list)
