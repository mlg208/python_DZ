class Smartphone:
    def __init__(self, brand, model, display_size, storage_capacity, battery_capacity, operating_system):
        self.brand = brand
        self.model = model
        self.display_size = display_size
        self.storage_capacity = storage_capacity
        self.battery_capacity = battery_capacity
        self.operating_system = operating_system

    def get_specifications(self):
        return f"{self.brand} {self.model} ({self.display_size}\", {self.storage_capacity}GB)"

    def check_battery_life(self, hours_of_usage):
        if hours_of_usage <= 0:
            return "Invalid input."
        battery_life = (self.battery_capacity / 1000) / hours_of_usage
        return f"Approximate battery life: {battery_life:.2f} days."

    def update_os(self, new_os):
        self.operating_system = new_os
        return f"Operating system updated to {new_os}."

    def is_android(self):
        return self.operating_system.lower() == "android"
