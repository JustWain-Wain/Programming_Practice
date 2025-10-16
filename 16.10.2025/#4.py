from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book: # Класс содержащий название книги, ее автора и год
    def __init__(self, title, author, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str: # Ф-ция выводит строку вида: Автор "Название", год
        return f'{self.author} "{self.title}", {self.year}г.'

    def __eq__(self, other) -> bool:
        return isinstance(other, Book) and self.title == other.title

    def __str__(self) -> str:
        return self.info()

    def print_info(self):
        print(self.info())

    @property
    def age(self):
        return datetime.now().year - int(self.year)

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(";")
        return cls(title, author, year)

class Ebook(Book): # Класс содержащий название электронной книги, ее автора и год
    def __init__(self, title, author, year: int):
        super().__init__(title, author, year)
        self.format = "Электронная книга"

    def info(self) -> str: # Ф-ция выводит строку вида: Автор "Название", год
        return f'{self.format}: {self.author} "{self.title}", {self.year}г.'

book1 = Book("Евгений Онегин", "А.С.Пушкин", 1833)
book2 = Ebook("Гарри Поттер", "Дж. Роулинг", 1997)
book3 = Book.from_string("Зов предков;Джек Лондон;1903")

print(book1, book2, book3, sep="\n")
book3.print_info()
print(book3.age)