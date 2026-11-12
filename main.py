from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("National Geographic", 101, 25)
dvd = DVD("Interstellar", 102, 169)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed book successfully:", book.describe())
except ValueError as e:
    print("Book already borrowed by someone:", e)


try:
    bob.borrow(book) # should fail: already borrowed
    print("Bob borrowed book successfully:", book.describe())
except ValueError as e:
    print("Book already borrowed by someone:", e)


# 2. Borrow-limit error
try:
    bob.borrow(magazine)
    print("Bob borrowed magazine successfully:", magazine.describe())
except ValueError as e:
    print("Borrow failed:", e)


try:
  bob.borrow(dvd)
  print("Bob borrowed DVD successfully:", dvd.describe())
except ValueError as e:
  print(f"Borrow failed: {e}")


# 3. Not-borrowed error
try:
  bob.return_item(book)
  print("Bob returned the book successfully")
except ValueError as e:
  print(f"Book was not borrowed, to return: {e}")


# 4. Successful return
try:
    alice.return_item(book)
    print("Alice returned the book successfully:", book.describe())
except ValueError as e:
    print("Return failed:", e)

# 5. Check availability and borrowed titles
print("Book available:", book.is_available())
print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())


# 6. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 7. Class attribute shared by all objects
print("Total items created:", LibraryItem.total_items)