# Создаем словарь для учета инвентаря
inventory = {
    "001": {"name": "Ноутбук", "quantity": 10, "price": 800},
    "002": {"name": "Смартфон", "quantity": 20, "price": 500},
    "003": {"name": "Планшет", "quantity": 15, "price": 300},
    "004": {"name": "Монитор", "quantity": 5, "price": 200},
}

# Вывод информации о товарах в инвентаре
for item_id, item_info in inventory.items():
    print(f"Артикул: {item_id}")
    print(f"Наименование: {item_info['name']}")
    print(f"Количество: {item_info['quantity']}")
    print(f"Цена: ${item_info['price']}")
    print()

# Добавление нового товара в инвентарь
new_item = {
    "name": "Клавиатура",
    "quantity": 8,
    "price": 30
}
inventory["005"] = new_item

# Обновление информации о товаре
item_id_to_update = "001"
inventory[item_id_to_update]["quantity"] -= 2
inventory[item_id_to_update]["price"] = 750

# Удаление товара из инвентаря
item_id_to_remove = "003"
if item_id_to_remove in inventory:
    del inventory[item_id_to_remove]

# Поиск товара по артикулу
search_item_id = "002"
if search_item_id in inventory:
    print(f"Товар с артикулом {search_item_id} найден:")
    print(f"Наименование: {inventory[search_item_id]['name']}")
else:
    print(f"Товар с артикулом {search_item_id} не найден.")

# Расчет общей стоимости инвентаря
total_value = sum(item_info["quantity"] * item_info["price"] for item_info in inventory.values())
print(f"Общая стоимость инвентаря: ${total_value}")
