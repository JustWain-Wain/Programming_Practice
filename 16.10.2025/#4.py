from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC): # Определяем обязательные функции, которые должны быть в каждом классе, наследующем Printable
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable): # Класс содержащий название книги, ее автора и год
    def __init__(self, title, author, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str: # Ф-ция выводит строку вида: "Автор "Название", год"
        return f'{self.author} "{self.title}", {self.year}г.'

    def __eq__(self, other) -> bool: # Заменяем встроенный в python результат операции ==
        return isinstance(other, Book) and self.title == other.title

    def __str__(self) -> str: # При print(book) будет выводиться info
        return self.info()

    def print_info(self): # Сразу печатает информацию на книге, но возвращает None
        print(self.info())

    @property
    def age(self): # Вычисляет возраст книги относительно года на данный момент
        return datetime.now().year - int(self.year)

    @classmethod
    def from_string(cls, data): # Дает возможность создать книгу, написав ее характеристики в виде "Название;Автор;Год"
        title, author, year = data.split(";")
        return cls(title, author, year)

class Ebook(Book): # Класс содержащий название электронной книги, ее автора и год, наследует от Book основные функции
    def __init__(self, title, author, year: int):
        super().__init__(title, author, year)
        self.format = "Электронная книга"

    def info(self) -> str: # Ф-ция выводит строку вида: "Электронная книга: Автор "Название", год"
        return f'{self.format}: {self.author} "{self.title}", {self.year}г.'

book1 = Book("Евгений Онегин", "А.С.Пушкин", 1833)
book2 = Ebook("Гарри Поттер", "Дж. Роулинг", 1997)
book3 = Book.from_string("Зов предков;Джек Лондон;1903")

print(book1, book2, book3, sep="\n")
book3.print_info()
print(book3.age)