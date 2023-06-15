number = input("Введите число: ")
shift = int(input("Введите количество цифр для сдвига: "))

if not number.isdigit():
    print("Ошибка! Введите число, состоящее только из цифр.")
    exit()

length = len(number)

if shift >= length:
    print("Ошибка! Количество цифр для сдвига превышает длину числа.")
    exit()

shifted_number = number[shift:] + number[:shift]

print("Результат сдвига:", shifted_number)
