class Book:
    def __init__(self, title, author, price, stock):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Price: ${self._price:.2f}")
        print(f"Stock: {self._stock} copies available")

    def update_stock(self, new_stock):
        self._stock = new_stock

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        self._title = new_title

    def get_author(self):
        return self._author

    def set_author(self, new_author):
        self._author = new_author

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        self._price = new_price

    def get_stock(self):
        return self._stock

    def set_stock(self, new_stock):
        self._stock = new_stock


