def calculate_distance(array):
    min_value = min(array)
    max_value = max(array)

    min_index = array.index(min_value)
    max_index = array.index(max_value)

    distance = abs(max_index - min_index)

    return distance

numbers = [3, 9, 8, 4, 5, 1]
distance = calculate_distance(numbers)

print("Расстояние между минимальным и максимальным числами:", distance)
