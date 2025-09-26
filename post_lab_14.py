















import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(7)
print("Circle Details")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
print("=" * 30)






class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 25)

    def apply_discount(self, discount_percent):
        discount_amount = self.price * (discount_percent / 100)
        self.price -= discount_amount


book1 = Book("Saraswatichandra", "Govardhanram Tripathi", 500)
book2 = Book("Manvini Bhavai", "Pannalal Patel", 750)

print("Book Details Before Discount:")
book1.display_details()
book2.display_details()

book2.apply_discount(10)

print("Book Details After Discount on Book 2:")
book1.display_details()
book2.display_details()
