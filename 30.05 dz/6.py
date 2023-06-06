sum = float(input("введите сумму покупки: "))
if sum < 200:
    discount = 0
elif sum < 300:
    discount = 0.03
elif sum < 500:
    discount = 0.05
else: 
    sum > 500
    discount = 0.07
total = sum * discount
total_sum = sum - total
print ("ваша сумма вместе со скидкой получилась ", total_sum)