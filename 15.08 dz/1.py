def bubble_sort(arr):
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
        n -= 1
    return arr

def select_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

user_input = input('Введите числа через запятую: ')
user_list = list(map(int, user_input.split(',')))

print("Исходный список:", user_list)

sorted_list = bubble_sort(user_list.copy())
print("Отсортированный список с помощью bubble_sort:", sorted_list)

sorted_list = select_sort(user_list.copy())
print("Отсортированный список с помощью select_sort:", sorted_list)

sorted_list = quick_sort(user_list.copy())
print("Отсортированный список с помощью quick_sort:", sorted_list)
