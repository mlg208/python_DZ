from person import Person
from car import Car
from book import Book
from product import Product
from smartphone import Smartphone
from movie import Movie

# Пример создания экземпляров и демонстрация работы

# Person
person1 = Person("Alice", 25, "female", 165, 60, "123 Main St")
print(person1.introduce())
print(person1.update_address("456 Elm St"))
print(f"BMI: {person1.get_bmi()}")
print(f"Is adult? {person1.is_adult()}")

# Car
car1 = Car("Toyota", "Camry", 2022, "blue", "gasoline", 25000)
print(car1.start_engine())
print(car1.get_description())
print(f"Tax: {car1.calculate_tax()}")
print(car1.repaint("red"))

# Book
book1 = Book("To Kill a Mockingbird", "Harper Lee", "Classics", 281, 1960, 5)
print(book1.get_info())
print(book1.rate(4))
print(f"Is a classic? {book1.is_classic()}")
print(book1.read(50))

# Product
product1 = Product("Laptop", 999, "Electronics", 10, "Dell", "15-inch display")
print(product1.display_info())
print(product1.restock(5))
print(product1.sell(3))
print(product1.update_description("17-inch display"))

# Smartphone
smartphone1 = Smartphone("Samsung", "Galaxy S21", 6.2, 128, 4000, "Android")
print(smartphone1.get_specifications())
print(smartphone1.check_battery_life(10))
print(smartphone1.update_os("Android 12"))
print(f"Is Android? {smartphone1.is_android()}")

# Movie
movie1 = Movie("Inception", "Christopher Nolan", "Science Fiction", 2010, 148, 4.5)
print(movie1.show_info())
print(movie1.rate_movie(5))
print(f"Is short? {movie1.is_short()}")
print(movie1.watch(120))
