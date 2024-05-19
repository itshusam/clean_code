from book import Book

my_book = Book("Python Programming", "John Doe", 25.99, 100)
my_book.display_info()
my_book.update_stock(80)
print(f"Updated stock quantity: {my_book.get_stock()}")
my_book.set_title("Python Programming for Beginners")
print(f"Updated title: {my_book.get_title()}")
my_book.set_price(29.99)
print(f"Updated price: ${my_book.get_price():.2f}")
my_book.set_author("Jane Smith")
print(f"Updated author: {my_book.get_author()}")