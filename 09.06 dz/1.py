start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

sum = 0
for num in range(start, end + 1):
    sum += num

print("Сумма всех чисел в диапазоне от", start, "до", end, "равна:", sum)
