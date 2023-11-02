class Product:
    def __init__(self, name, price, category, stock_quantity, brand, description):
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        self.brand = brand
        self.description = description

    def display_info(self):
        return f"{self.name} ({self.brand}): {self.price} USD"

    def restock(self, quantity_to_add):
        self.stock_quantity += quantity_to_add
        return f"Added {quantity_to_add} to stock. New stock quantity: {self.stock_quantity}."

    def sell(self, quantity_to_sell):
        if quantity_to_sell <= self.stock_quantity:
            self.stock_quantity -= quantity_to_sell
            return f"Sold {quantity_to_sell} units. Remaining stock: {self.stock_quantity}."
        else:
            return "Not enough stock to sell."

    def update_description(self, new_description):
        self.description = new_description
        return "Description updated."
