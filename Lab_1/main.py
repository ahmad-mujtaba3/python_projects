from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def display(self):
        pass


class Member(Person):
    def display(self):
        print("Member:", self.name, self.person_id)


class Librarian(Person):
    def display(self):
        print("Librarian:", self.name, self.person_id)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Loan:
    def __init__(self, member, book):
        self.member = member
        self.book = book


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, book):
        if book in self.books and book.available:
            self.loans.append(Loan(member, book))
            book.available = False
            print("Book borrowed!")
        else:
            print("Book not available!")

    def show_books(self):
        for book in self.books:
            print(book.title, "-", "Available" if book.available else "Borrowed")


library = Library()

librarian = Librarian("Ahmad", 1)
member = Member("Ali", 101)

library.add_member(member)
library.add_book(Book("Python Programming", "John Smith"))
library.add_book(Book("Java Basics", "James Gosling"))

librarian.display()
member.display()

library.show_books()
library.borrow_book(member, library.books[0])
library.show_books()