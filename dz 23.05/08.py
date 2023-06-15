purchase_price = float(input("Введите стоимость покупки ($): "))
discount = float(input("Введите размер скидки (%): "))

discount_amount = purchase_price * (discount / 100)
total_amount = purchase_price - discount_amount

print("Сумма скидки: ${:.2f}".format(discount_amount))
print("Итоговая сумма к оплате: ${:.2f}".format(total_amount))
