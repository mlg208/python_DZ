# Функция возвращает результат деления большего по модулю числа на меньшее.
def smart_div(num1, num2=None):
    if num2 is None:
        anum1 = abs(num1)
        return num1/num1
    anum1 = abs(num1)
    anum2 = abs(num2)
    
    if anum1 > anum2:
        return num1/num2
    elif num2 < num1:
        return num2/num1
    else:
        num2 = num1
        return num1/num1
    


def test_smart_div():
    assert smart_div(20, 4) ==  5
    assert smart_div(3, -6) == -2
    assert smart_div(-8)    ==  1
    
test_smart_div()