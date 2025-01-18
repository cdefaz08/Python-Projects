class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)
    
    def show_books(self):
        for book in self.books:
            print(f"Title: {book.title} Author: {book.author} Available: {book.available}")
    
    def show_users(self):
        for user in self.users:
            print(f"Name: {user.name} User ID: {user.user_id}")

# Create book and user instances
book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("The Da Vinci Code", "Dan Brown")
book3 = Book("The Catcher in the Rye", "J.D. Salinger")

user1 = User("John", 1)
user2 = User("Jane", 2)
user3 = User("Doe", 3)

# Create a library object
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_user(user1)
library.add_user(user2)
library.add_user(user3)

# Show books and users
library.show_books()
library.show_users()