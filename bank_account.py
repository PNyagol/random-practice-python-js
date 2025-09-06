class Product:
    all_products = []

    def __init__(self, name, price, category, stock=0):
        self._name = name
        self._price = price
        self._stock = stock
        self._category = category
        self._reviews = []
        Product.all_products.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name.strip():
            raise ValueError("Product name cannot be empty")
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @property
    def stock(self):
        return self._stock

    def add_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Stock quantity must be positive")
        self._stock += quantity

    def remove_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Stock quantity must be positive")
        if quantity > self._stock:
            raise ValueError("Not enough stock available")
        self._stock -= quantity

    def add_review(self, rating, comment=""):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._reviews.append({"rating": rating, "comment": comment})

    @property
    def average_rating(self):
        if not self._reviews:
            return 0
        return sum(review["rating"] for review in self._reviews) / len(self._reviews)

    @classmethod
    def get_products_by_category(cls, category):
        return [product for product in cls.all_products if product._category.lower() == category.lower()]

    @classmethod
    def get_low_stock_products(cls, threshold=5):
        return [product for product in cls.all_products if product.stock < threshold]

    @classmethod
    def get_top_rated_products(cls, min_reviews=3):
        return sorted(
            [product for product in cls.all_products if len(product._reviews) >= min_reviews],
            key=lambda p: p.average_rating,
            reverse=True
        )[:5]

    @staticmethod
    def format_price(price):
        return f"${price:.2f}"

    @staticmethod
    def validate_category(category):
        valid_categories = ["electronics", "clothing", "books", "home", "sports"]
        return category.lower() in valid_categories

    def __str__(self):
        return f"{self._name} ({Product.format_price(self._price)}) - Category: {self._category}, Stock: {self._stock}"


# --------------------- #
# Example Usage
# --------------------- #

# Create some products
laptop = Product("Laptop", 30000, "electronics", 15)
phone = Product("Smartphone", 16700, "electronics", 5)
book = Product("Python Lesson", 255, "books", 20)
shirt = Product("T-Shirt", 45, "clothing", 2)

# Add reviews
laptop.add_review(5, "Great laptop!")
laptop.add_review(4, "Good performance")
phone.add_review(3, "Average phone")
book.add_review(5, "Excellent for learning Python")
shirt.add_review(2, "Poor quality")

# Using class methods
electronics = Product.get_products_by_category("electronics")
print("Electronics products:")
for product in electronics:
    print(f"  - {product.name}")

low_stock = Product.get_low_stock_products()
print("\nLow stock products:")
for product in low_stock:
    print(f"  - {product.name} (Stock: {product.stock})")

# Top-rated products
top_rated = Product.get_top_rated_products()
print("\nTop-rated products:")
for product in top_rated:
    print(f"  - {product.name} (Rating: {product.average_rating:.1f})")

# Using static methods
print("\nStatic method examples:")
print(Product.format_price(19.99))
print(Product.validate_category("electronics"))
print(Product.validate_category("food"))

# Using properties with validation
try:
    laptop.price = -100
except ValueError as e:
    print(f"\nError: {e}")

# Printing product objects (thanks to __str__)
print("\nProduct details:")
print(laptop)
print(phone)
print(book)
print(shirt)
